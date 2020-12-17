# BiorxivRetriever
Simple python retriever for Biorxiv articles.

# Purpose
Given a text query, search for relevant papers on Biorxiv and get their links and content.

# Install

Install with pip:
```
pip install biorxiv_retriever
```

Alternatively, clone this repo and install:
```
git clone https://github.com/TalSchuster/BiorxivRetriever.git
python setup.py install
```

# API
```
from biorxiv_retriever import BiorxivRetriever
br = BiorxivRetriever()
papers = br.query('covid remdesivir')
```
To get only titles and links without metadata and full text (when possible):
```
papers = br.query('covid remdesivir', metadata=False, full_text=False)
```

To use [Rxivist](https://www.rxivist.org/) as the search engine (provides extra metadata but doesn't have all papers):
```
br = BiorxivRetriever(search_engine='rxivist')
```

# Output

Example output:
```
[
{'title': 'Enisamium is a small molecule inhibitor of the influenza A virus and SARS-CoV-2 RNA polymerases',
'biorxiv_url': 'https://www.biorxiv.org//content/10.1101/2020.04.21.053017v2',
'posted': 'May 11, 2020.',
'abstract': 'Abstract Influenza A virus and coronavirus strains cause a mild to severe respiratory disease that can result in death. Although vaccines exist against circulating influenza A viruses, such vaccines are ineffective against emerging pandemic influenza A viruses. Currently, no vaccine exists against coronavirus infections, including pandemic SARS-CoV-2, the causative agent of the Coronavirus Disease 2019 (COVID-19). To combat these RNA virus infections, alternative antiviral strategies are needed. A key drug target is the viral RNA polymerase, which is responsible for viral RNA synthesis. In January 2020, the World Health Organisation identified enisamium as a candidate therapeutic against SARS-CoV-2. Enisamium is an isonicotinic acid derivative that is an inhibitor of multiple influenza B and A virus strains in cell culture and clinically approved in 11 countries. Here we show using in vitro assays that enisamium and its putative metabolite, VR17-04, inhibit the activity of the influenza virus and the SARS-CoV-2 RNA polymerase. VR17-04 displays similar efficacy against the SARS-CoV-2 RNA polymerase as the nucleotide analogue remdesivir triphosphate. These results suggest that enisamium is a broad-spectrum small molecule inhibitor of RNA virus RNA synthesis, and implicate it as a possible therapeutic option for treating SARS-CoV-2 infection. Unlike remdesivir, enisamium does not require intravenous administration which may be advantageous for the development of COVID-19 treatments outside a hospital setting.',
'full_text': '...'}
]
```
