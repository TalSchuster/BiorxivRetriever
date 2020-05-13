from distutils.core import setup
setup(
  name = 'biorxiv_retriever',
  packages = ['biorxiv_retriever'],
  version = '0.1',
  license='MIT',
  description = 'Simple retriever for Biorxiv articles',
  author = 'Tal Schuster',
  author_email = 'my.email@mit.edu',
  url = 'https://github.com/TalSchuster/BiorxivRetriever/biorxiv_retriever',
  download_url = 'https://github.com/TalSchuster/BiorxivRetriever/biorxiv_retriever/v_01.tar.gz',
  keywords = ['Biology', 'Rxivist', 'Biorxiv', 'retriever'],
  install_requires=[
          'tqdm',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
