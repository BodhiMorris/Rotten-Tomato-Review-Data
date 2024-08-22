# Setup of pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
x = 0

# Making dataframe, cleaning and analysing
rotten_reviews_df = pd.read_csv('data/rotten_tomatoes_movie_reviews.csv', on_bad_lines='warn' )
rotten_reviews_df.drop(columns=['criticName', 'reviewUrl', 'publicatioName', 'reviewText'], inplace=True)
rotten_reviews_df = rotten_reviews_df[rotten_reviews_df['isTopCritic'] == True]
rotten_reviews_df.dropna(inplace=True)
rotten_reviews_df = rotten_reviews_df.query(f'originalScore.str.contains("/")', engine='python')
rotten_reviews_df.drop(columns=['reviewId'], inplace=True)

rotten_reviews_df = rotten_reviews_df.query(f'not originalScore.str.contains(" ")', engine='python') #clean
rotten_reviews_df = rotten_reviews_df.query(f'not originalScore.str.contains("`")', engine='python') #clean
rotten_reviews_df = rotten_reviews_df.query(f'not originalScore.str.contains("/4/")', engine='python') #clean
rotten_reviews_df = rotten_reviews_df.query(f'not originalScore.str.contains("f")', engine='python') #clean
rotten_reviews_df = rotten_reviews_df.query(f'not originalScore.str.contains("a")', engine='python') #clean
rotten_reviews_df['originalScore'] = rotten_reviews_df['originalScore'].str.replace("'", '')
rotten_reviews_df.drop(rotten_reviews_df.index[192242], inplace=True)

#---------------------------------------------------------------------------------------------------------------------------------------

rotten_reviews_df[['score', 'diviser']] = rotten_reviews_df['originalScore'].str.split('/', n=1, expand=True)
rotten_reviews_df.dropna(inplace=True)
rotten_reviews_df.drop(rotten_reviews_df.index[95363:95364], inplace=True)

rotten_reviews_df['score'] = rotten_reviews_df['score'].astype(float)
rotten_reviews_df['diviser'] = rotten_reviews_df['diviser'].astype(float)

rotten_reviews_df['percentScore'] = rotten_reviews_df['score']/rotten_reviews_df['diviser']*100
rotten_reviews_df.drop(columns=['originalScore', 'score', 'diviser'], inplace=True)

#---------------------------------------------------------------------------------------------------------------------------------------

averagedScore_df = rotten_reviews_df.drop(columns=['creationDate','isTopCritic','reviewState','scoreSentiment'])
averagedScore_df = averagedScore_df.groupby(['id']).mean()
averagedScore_df = averagedScore_df.reset_index()
averagedScore_df = averagedScore_df.round(2)

#---------------------------------------------------------------------------------------------------------------------------------------

id_df = rotten_reviews_df.drop(columns=['isTopCritic','reviewState','scoreSentiment','percentScore'])
id_df['id'] = id_df['id'].drop_duplicates()
id_df.dropna(inplace=True)
id_df.sort_values(by=['id'], inplace=True)
id_df = id_df.reset_index()

#---------------------------------------------------------------------------------------------------------------------------------------

final_data_df = pd.DataFrame(columns=['id', 'score', 'date'])

final_data_df['date'] = id_df['creationDate']
final_data_df['id'] = averagedScore_df['id']
final_data_df['score'] = averagedScore_df['percentScore']
final_data_df.sort_values(by=['date'], inplace=True)

#---------------------------------------------------------------------------------------------------------------------------------------

def showFinalData():
    print(final_data_df)
    userOptions()

#---------------------------------------------------------------------------------------------------------------------------------------
    
def saveFinalData():
    final_data_df.to_csv('data/Final Dataset.csv', index=False)
    userOptions()


#---------------------------------------------------------------------------------------------------------------------------------------
    
def showChart():
    print("""The full dataset is too large to visualise so please enter a date to show
          
          The date is YYYY-MM-DD
          You can do things like 2023-07 to show all of july""")
    try:
        date = input('Please enter date: ')
        test_data_df = final_data_df[final_data_df['date'].str.contains(date)]
        test_data_df.plot(
                    kind='bar',
                    x='date',
                    y='score',
                    color='blue',
                    alpha=0.3,
                    title='Movie Reviews Compared to Time')
        plt.show()
        userOptions()
    except:
        print('Your date was invalid, please try again')
        showChart()

#---------------------------------------------------------------------------------------------------------------------------------------

def searchMovie():
    print("""Movie names are formated all lower case and with spaces replaced with underscores, type leave to go back
          
    This shows all movies containing whatever word you put in, e.g spiderman shows spiderman, spiderman_2 and spiderman_3
    """)
    
    movieName = str(input('Please input a movie name: '))
    if movieName == 'leave':
        userOptions()
    else:
        print(final_data_df[final_data_df['id'].str.contains(movieName)])
        searchMovie()

#---------------------------------------------------------------------------------------------------------------------------------------



def userOptions():
    global quit

    print("""Rotten Tomatoes Movie Reviews
          
    Please select an option:
    1 - Show the final dataset
    2 - Save the final dataset
    3 - See visualisation
    4 - Search for a movie
    5 - Quit Program
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showFinalData()
        elif choice == 2:
            saveFinalData()
        elif choice == 3:
            showChart()
        elif choice == 4:
            searchMovie()
        elif choice == 5:
            print('bye')
        else:
            print('Try again, that number isnt between 1 & 4')
            userOptions()

    except:
        print('Please try again')
        userOptions()

#---------------------------------------------------------------------------------------------------------------------------------------

userOptions()
