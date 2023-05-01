import glob
import pandas as pd

df = pd.DataFrame(columns=['Month', 'Total Hate Speech Tweets', 'Proportion of Hate Speech Tweets', 'Weekly Average of Hate Speech Tweets', 'Average Likes on Hate Speech', 'Average Retweets on Hate Speech', 'Average Replies on Hate Speech', 'Average Quotes on Hate Speech'])

month_names = ['jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'jan', 'feb', 'mar']
full_month_names = ['June', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'February', 'March']
m=0

weeks = ['week1', 'week2', 'week3', 'week4']

while (m < 10):
    w=0

    monthly_hate_tweets = 0 # num of tweets classified as hate speech
    tweets_in_this_month = 0 # sum of tweets classified as hate speech + offensive + neutral
    weekly_avg_hate_tweets = []
    
    # engagement on hate tweets
    total_likes = 0
    total_retweets = 0
    total_replies = 0
    total_quotes = 0

    while (w < 4):
        if month_names[m] == "oct" and weeks[w] == "week4":
            csv_files = glob.glob('oct-week4*.{}'.format('csv'))
            temp_df = pd.DataFrame()
            for file in csv_files:
                temp_df = pd.concat([temp_df,pd.read_csv(file)])
        else:
            temp_df = pd.read_csv(month_names[m] + '-' + weeks[w] + '-classified50.csv')
        

        ##### drop dupes

        temp_df = temp_df[["User", "Date Created", "Number of Likes", "Number of Retweets", "Number of Replies", "Number of Quotes", "Number of Views", "Tweet", "class"]]
        temp_df = temp_df.drop_duplicates()

        hate_tweets_in_week = temp_df['class'].value_counts()[0]
        total_tweets_in_week = temp_df.shape[0]
        
        monthly_hate_tweets += hate_tweets_in_week
        tweets_in_this_month += total_tweets_in_week
        weekly_avg_hate_tweets.append(hate_tweets_in_week / total_tweets_in_week)

        temp_df = temp_df.loc[temp_df['class'] == 0]
        total_likes += temp_df['Number of Likes'].sum()
        total_retweets += temp_df['Number of Retweets'].sum()
        total_replies += temp_df['Number of Replies'].sum()
        total_quotes += temp_df['Number of Quotes'].sum()


        w += 1

    
    calculate_weekly_avg_hate_tweets = sum(weekly_avg_hate_tweets) / 4

    df2 = {'Month': [full_month_names[m]], 
           'Total Hate Speech Tweets': [monthly_hate_tweets],
            'Proportion of Hate Speech Tweets': [monthly_hate_tweets/tweets_in_this_month],
            'Weekly Average of Hate Speech Tweets': [calculate_weekly_avg_hate_tweets], 
            'Average Likes on Hate Speech': [total_likes / monthly_hate_tweets], 
            'Average Retweets on Hate Speech': [total_retweets / monthly_hate_tweets], 
            'Average Replies on Hate Speech':[total_replies / monthly_hate_tweets], 
            'Average Quotes on Hate Speech': [total_quotes / monthly_hate_tweets]}
    df2 = pd.DataFrame(df2)

    #df = df.append(df2, ignore_index = True)
    df = pd.concat([df, df2], axis=0)

    m += 1

#df.to_csv('summary-results.csv')














