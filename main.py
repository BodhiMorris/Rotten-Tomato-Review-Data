# Setup of pandas and matplotlib
import pandas as pd


# Making dataframe, cleaning and analysing
#rotten_reviews_df = pd.read_csv('data/rotten_tomatoes_movie_reviews.csv', on_bad_lines='warn' )
#rotten_reviews_df.drop(columns=['criticName', 'reviewUrl', 'publicatioName', 'reviewText'], inplace=True)
#rotten_reviews_df = rotten_reviews_df[rotten_reviews_df['isTopCritic'] == True]
#rotten_reviews_df.dropna(inplace=True)
#rotten_reviews_df = rotten_reviews_df.query(f'originalScore.str.contains("/")', engine='python')
###rotten_reviews_df = rotten_reviews_df[rotten_reviews_df['originalScore'] * 100]

#rotten_reviews_df['originalScore'].duplicated.mean() #Try to average duplicate ids

##print(rotten_reviews_df)

##rotten_reviews_df.to_csv('data/cleaned data.csv', index=False)
rotten_reviews_df = pd.read_csv('data/cleaned data.csv', on_bad_lines='warn' )
rotten_reviews_df['originalScore'] = rotten_reviews_df['originalScore'].str.replace('/5', '')
rotten_reviews_df['originalScore'] = rotten_reviews_df['originalScore'].str.replace('/4', '')



#rotten_reviews_df = rotten_reviews_df.query(f'not originalScore.str.contains(".")', engine='python')
#rotten_reviews_df['originalScore'] = rotten_reviews_df['originalScore'].astype(float)
print(rotten_reviews_df)
