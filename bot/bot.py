import time
from sqlalchemy import create_engine
import requests
import os


time.sleep(12)

pg = create_engine('postgresql://postgres:1234@project_postgresdb_1:5432/tweets')
webhook_url = os.environ['WEBHOOK']


query = "SELECT * FROM TWEETS LIMIT 3;"

sqlquery = pg.execute(query)

for s in sqlquery:
    text = str(f'For the tweet: \n {s[0]} \n The sentiment is: {s[1]}') #is string necessary?
    print(text)
#    print(text)
    data = {'text': text}
#    requests.post(url = webhook_url, json = data)
    time.sleep(5)