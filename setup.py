from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'biorxiv_retriever',
  #packages = ['biorxiv_retriever'],
  packages = find_packages(),
  version = '0.20.1',
  license='MIT',
  description = 'Simple retriever for Biorxiv articles',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Tal Schuster',
  author_email = 'my.email@mit.edu',
  url = 'https://github.com/TalSchuster/BiorxivRetriever/',
  download_url = 'https://github.com/TalSchuster/BiorxivRetriever/biorxiv_retriever/v_0_20_1.tar.gz',
  keywords = ['Biology', 'Rxivist', 'Biorxiv', 'retriever'],
  install_requires=[
          'tqdm',
          'lxml',
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
