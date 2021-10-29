import twint
import datetime
import string
import nest_asyncio
nest_asyncio.apply()

def clean_input(hashtag):
    clean_user_text = ''
    for char in hashtag:
        if char not in string.punctuation and char.isalpha():
            clean_user_text += char
    clean_user_text_no_space = clean_user_text.replace(' ', '')
    return clean_user_text_no_space

def get_tweet(tag:str,limit:int,language="en"):
    since = datetime.datetime(2020, 1, 1)
    until = datetime.datetime(2021, 5, 1)

    config = twint.Config()
    config.Search = tag
    config.Lang = language
    config.Limit = limit
    config.Since = str(since)
    config.Pandas = True
    
    #TODO : more date for more data
    """ days = [7,14,21,28]

    for month in range(9,11):
        for day in days:
            until = datetime.datetime(2021, month, day)
            config.Until = str(until) """
    
    twint.run.Search(config)
    return  twint.storage.panda.Tweets_df