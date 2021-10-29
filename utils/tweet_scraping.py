import twint
import datetime
import nest_asyncio
nest_asyncio.apply()

def get_tweet(tag:str,limit:int,language="en"):
    since = datetime.datetime(2020, 1, 1)
    until = datetime.datetime(2021, 5, 1)

    config = twint.Config()
    config.Search = tag
    config.Lang = language
    config.Limit = limit
    config.Since = str(since)
    config.Output = "SquidGames.csv"

    days = [7,14,21,28]

    for month in range(9,11):
        for day in days:
            until = datetime.datetime(2021, month, day)
            config.Until = str(until)
            twint.run.Search(config)

    return 