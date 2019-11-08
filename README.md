# IMDB-Movie-Recommender
Content based movie recommender

Packages used: pandas, numpy, nltk, sklearn, matplotlib, selenium, re

Series of Jupyter notebooks:

1. IMDB_Selenium_scraper.ipynb

  I scraped data from the IMDB website using the selenium package in Python. 
  I first used Selenium to do e2e integration tests during my internship in SAP.
  I tranferred these skills over to scrpae data.
  
2. Data_Cleaning_Feature_Engineering.ipynb

  I engineered features from genre, director, actor, storyline and production company
  I saved features in seperate pickles
  
3. Movie_Recommender.ipynb

  I created a movie similarity matrix using the cosine similarity between movies
  I created a method to display the most similiar movies to another

4. PCA_similarity_recommender.ipynb

  I redcued the dimensionality of our dataset to enable better similarity scores

5. title_char_based_predictions.ipynb

  I built a character level language model using Keras LSTM to predict a word from title based a small number of characters         from that title. 
  I used a 2 character look-ahead method by maximizing the product of the probabilites of the next 2 characters.
  I used an ipywidget to dynamically update the input and produce the latest predicted word
