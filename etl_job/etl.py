
import logging
import pymongo
import time
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# check whether everything is OK
logging.critical("Hello World - from ETL")

#give it a bit of time
time.sleep(6)

#initiate the sentimentanalyze for the docs file
s  = SentimentIntensityAnalyzer()

#now the code
client = pymongo.MongoClient(host="mongodb", port=27017)
db = client.twitter

pg = create_engine('postgresql://postgres:1234@project_postgresdb_1:5432/tweets')

pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(500),
    sentiment NUMERIC
);
''')


docs = db.tweets.find()
for doc in docs:
    text = doc['text'].replace('\n', '')
    query = "INSERT INTO TWEETS values (%s, %s);"
    sentiment = s.polarity_scores(doc['text'])
    score = sentiment['compound']
    pg.execute(query, (text, score))

