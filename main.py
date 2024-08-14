# Setup of pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Making dataframe, cleaning and analysing
rotten_reviews_df = pd.read_csv('data/rotten_tomatoes_movie_reviews.csv')
rotten_reviews_df.drop(columns=['criticName', 'reviewUrl', 'publicatioName'], inplace=True)
rotten_reviews_df = rotten_reviews_df[rotten_reviews_df['isTopCritic'] == 'True']
rotten_reviews_df = rotten_reviews_df[rotten_reviews_df['originalScore'] =! '']
rotten_reviews_df = rotten_reviews_df[rotten_reviews_df['originalScore'] =! float]