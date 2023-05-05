# Natural-Language-Processing-NLP
Data extraction and analysis using: pandas, beautiful soup, NumPy, plotly express ...

The goal of the project is to collect data from the website (on the topic of COVID-19).

I realized the project using three programs:

(1) final.py - Enables web scraping by all categories, i.e. subpages of the web site (I implemented an interactive menu in the CLI/Terminal of the IDE 
with which the user can set the program as needed).


After successful data scraping, the user can start the data analysis found in the program:

(2) keywordSearch.py - words and categories of the COVID-19 topic are defined, which refine the csv file (data set created in the previous step) 
[approx. 25640 articles from 2019 to 2023]. Then the most interesting words of the COVID-19 theme are reviewed and I illustrate them using WordArt, 
I also implemented dynamic and interactive graphs with the possibility of viewing data by intervals.

![Word_cloud_eVaraždin](https://user-images.githubusercontent.com/96542493/236576230-d5aa7a96-0e9e-49e0-8218-f419f354caab.png)

*Bigger words == more times mentioned*

![CleanShot 2023-05-06 at 00 06 11](https://user-images.githubusercontent.com/96542493/236576634-a9c526a8-d997-4ca9-9638-1336d9254ac0.gif)

*An interactive graph that enables precise definition, number of articles at specific period, their topic and publication date*

(3) merge and jaccard.py - using the sklearn.metrics library I use jaccard_score to determine adjacency and features in each sentence (intercomparison).
