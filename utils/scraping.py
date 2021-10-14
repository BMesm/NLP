import twint
import datetime
import nest_asyncio
nest_asyncio.apply()

since = datetime.datetime(2020, 1, 1)
until = datetime.datetime(2021, 5, 1)

#configuration
config = twint.Config()
config.Search = "SquidGames"
config.Lang = "en"
config.Limit = 30000
config.Since = str(since)
config.Output = "SquidGames.csv"



days = [7,14,21,28]

for month in range(9,11):
    for day in days:
        until = datetime.datetime(2021, month, day)
        config.Until = str(until)
        twint.run.Search(config)
