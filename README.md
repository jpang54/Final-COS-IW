# COS IW Files

This repository contains files for my Spring 2023 COS IW: Amending Section 230 Based on Twitter Hate Speech Trends.

train_classifier.ipynb, classifier.py, labeled_data.csv, and refined_ngram_dict.csv are originally from [Davidson et al. (2017)'s repository.](https://github.com/t-davidson/hate-speech-and-offensive-language)

The files train_classifier.ipynb and classifier.py were modified to account for package version changes since 2017.

The folder classified-csvs contains the labeled scraped tweets. 

scrape.py used the Snscrape API to scrape tweets off Twitter. 

summary-results.csv is produced by summary.py and shows the trends in hate speech and engagement with it.
