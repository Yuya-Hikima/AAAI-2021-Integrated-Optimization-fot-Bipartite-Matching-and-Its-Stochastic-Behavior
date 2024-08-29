import requests

url='https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2019-10.parquet'
filename='../data/green_tripdata_2019-10.parquet'
urlData = requests.get(url).content
with open(filename ,mode='wb') as f:
    f.write(urlData)

url='https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2019-10.parquet'
filename='../data/yellow_tripdata_2019-10.parquet'
urlData = requests.get(url).content
with open(filename ,mode='wb') as f:
    f.write(urlData)

import sys
import pandas
df = pandas.read_parquet('../data/green_tripdata_2019-10.parquet')
df.to_csv('../data/green_tripdata_2019-10.csv',index=True)

import sys
import pandas
df = pandas.read_parquet('../data/yellow_tripdata_2019-10.parquet')
df.to_csv('../data/yellow_tripdata_2019-10.csv',index=True)
