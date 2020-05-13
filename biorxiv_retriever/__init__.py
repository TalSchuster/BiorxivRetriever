import json
from urllib import request
from bs4 import BeautifulSoup
from tqdm import tqdm
"""
Simple helper to retrieve biorxiv articles for a given search query.
"""

DEFAULT_URL = {
    'rxivist':
    'https://api.rxivist.org/v1/papers?q={}&timeframe=alltime&metric=downloads&page_size=100&page={}',
    'biorxiv':
    'https://www.biorxiv.org/search/{}%20numresults%3A25%20sort%3Apublication-date%20direction%3Adescending'
}


class BiorxivRetriever():
    def __init__(self, search_engine='biorxiv', search_url=None):
        assert search_engine in ['biorxiv', 'rxivist']
        self.search_engine = search_engine
        self.serach_url = search_url or DEFAULT_URL[search_engine]
        return

    def _get_article_content(self,
                             page_soup,
                             exclude=[
                                 'abstract', 'ack', 'fn-group', 'ref-list'
                             ]):
        article = page_soup.find("div", {'class': 'article'})
        article_txt = ""
        if article is not None:
            for section in article.children:
                if section.has_attr('class') and any(
                        [ex in section.get('class') for ex in exclude]):
                    continue
                article_txt += section.get_text(' ')

        return article_txt

    def _get_all_links(self, page_soup, base_url="https://www.biorxiv.org"):
        links = []
        for link in page_soup.find_all(
                "a", {"class": "highwire-cite-linked-title"}):
            uri = link.get('href')
            links.append({'title': link.text, 'biorxiv_url': base_url + uri})

        return links

    def _get_papers_list_rxivist(self, query):
        papers = []
        for i in range(0, 100):
            url = self.serach_url.format(query, i)
            data = json.loads(request.urlopen(url).read().decode("utf-8"))
            if len(data['results']) == 0:
                break

            papers.extend(data['results'])

        return papers

    def _get_papers_list_biorxiv(self, query):
        papers = []
        url = self.serach_url.format(query)
        page_html = request.urlopen(url).read().decode("utf-8")
        page_soup = BeautifulSoup(page_html, "lxml")
        links = self._get_all_links(page_soup)
        papers.extend(links)

        page_links = page_soup.find_all("li", {"class": "pager-item"})
        if len(page_links) > 0:
            num_pages = int(page_links[-1].text)
            for i in range(1, num_pages):
                page_url = url + '?page={}'.format(i)
                page_html = request.urlopen(page_url).read().decode("utf-8")
                page_soup = BeautifulSoup(page_html, "lxml")
                links = self._get_all_links(page_soup)
                papers.extend(links)

        return papers

    def query(self, query, metadata=True, full_text=True):
        query = query.replace(' ', '%20')

        if self.search_engine == 'rxivist':
            papers = self._get_papers_list_rxivist(query)
        elif self.search_engine == 'biorxiv':
            papers = self._get_papers_list_biorxiv(query)
        else:
            raise Exception('None implemeted search engine: {}'.format(
                self.search_engine))

        if metadata or full_text:
            for paper in tqdm(papers):
                biorxiv_url = paper['biorxiv_url'] + '.full'
                page_html = request.urlopen(biorxiv_url).read().decode("utf-8")
                page_soup = BeautifulSoup(page_html, "lxml")
                if metadata:
                    date = page_soup.find("div", {"class": "pane-1"})
                    if date is not None:
                        date_str = date.text.split('\xa0')[-1].strip()
                        paper['posted'] = date_str
                    else:
                        paper['posted'] = ''

                    abstract = page_soup.find("div", {
                        'class': 'abstract'
                    }).get_text(' ')
                    paper['abstract'] = abstract

                if full_text:
                    article_txt = self._get_article_content(page_soup)
                    paper['full_text'] = article_txt

        return papers
