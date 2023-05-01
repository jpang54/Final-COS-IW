import snscrape.modules.twitter as sntwitter
import pandas as pd

# Time range from June 2022 to Mar 2023 for csv file naming
j = 0
month_names = ['jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'jan', 'feb', 'mar']

# Date ranges; until is exclusive
june_weeks_since = ['2022-06-01', '2022-06-08', '2022-06-15', '2022-06-22']
june_weeks_until = ['2022-06-08', '2022-06-15', '2022-06-22', '2022-07-01']

july_weeks_since = ['2022-07-01', '2022-07-08', '2022-07-15', '2022-07-22']
july_weeks_until = ['2022-07-08', '2022-07-15', '2022-07-22', '2022-08-01']

aug_weeks_since = ['2022-08-01', '2022-08-08', '2022-08-15', '2022-08-22']
aug_weeks_until = ['2022-08-08', '2022-08-15', '2022-08-22', '2022-09-01']

sept_weeks_since = ['2022-09-01', '2022-09-08', '2022-09-15', '2022-09-22']
sept_weeks_until = ['2022-09-08', '2022-09-15', '2022-09-22', '2022-10-01']

oct_weeks_since = ['2022-10-01', '2022-10-08', '2022-10-15', '2022-10-22']
oct_weeks_until = ['2022-10-08', '2022-10-15', '2022-10-22', '2022-11-01']

nov_weeks_since = ['2022-11-01', '2022-11-08', '2022-11-15', '2022-11-22']
nov_weeks_until = ['2022-11-08', '2022-11-15', '2022-11-22', '2022-12-01']

dec_weeks_since = ['2022-12-01', '2022-12-08', '2022-12-15', '2022-12-22']
dec_weeks_until = ['2022-12-08', '2022-12-15', '2022-12-22', '2023-01-01']

jan_weeks_since = ['2023-01-01', '2023-01-08', '2023-01-15', '2023-01-22']
jan_weeks_until = ['2023-01-08', '2023-01-15', '2023-01-22', '2023-02-01']

feb_weeks_since = ['2023-02-01', '2023-02-08', '2023-02-15', '2023-02-22']
feb_weeks_until = ['2023-02-08', '2023-02-15', '2023-02-22', '2023-03-01']

mar_weeks_since = ['2023-03-01', '2023-03-08', '2023-03-15', '2023-03-22']
mar_weeks_until = ['2023-03-08', '2023-03-15', '2023-03-22', '2023-04-01']

since = [june_weeks_since, july_weeks_since, aug_weeks_since, sept_weeks_since, oct_weeks_since, nov_weeks_since, dec_weeks_since, jan_weeks_since, feb_weeks_since, mar_weeks_since]
until = [june_weeks_until, july_weeks_until, aug_weeks_until, sept_weeks_until, oct_weeks_until, nov_weeks_until, dec_weeks_until, jan_weeks_until, feb_weeks_until, mar_weeks_until]

# Read in keywords
keywords_df = pd.read_csv('refined_ngram_dict.csv') 
keyword_index = 0

# Loop from June to March
while j < 10:

    k = 0
    n = len(since[j])

    # Loop through the weeks in each month
    while k < n:

        while keyword_index < 178:
            # Creating list to append tweet data to
            attributes_container = []

            # Using TwitterSearchScraper to scrape data and append tweets to list
            for i,tweet in enumerate(sntwitter.TwitterSearchScraper(str(keywords_df['ngram'].values[keyword_index]) + ' since:' + since[j][k] + ' until:' + until[j][k] + ' lang:en', mode = sntwitter.TwitterSearchScraperMode.TOP).get_items()):
                if i>500:
                    break
                attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.retweetCount, tweet.replyCount, tweet.quoteCount, tweet.viewCount, tweet.rawContent])
                
            # Creating a dataframe to load the list
            tweets_df = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Number of Retweets", "Number of Replies", "Number of Quotes", "Number of Views", "Tweet"])


            file_name = month_names[j] + '-week' + str(k+1) + '-' + str(keyword_index) + '.csv'
            tweets_df.to_csv(file_name)

            keyword_index += 1
        k += 1
        keyword_index = 0

    j += 1
    keyword_index = 0


