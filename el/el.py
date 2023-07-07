import os
import json
import requests
import datetime
import logging
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, types
from sqlalchemy.dialects.postgresql import JSON as postgres_json
from sqlalchemy_utils import database_exists, create_database

# load in environment variables
load_dotenv()

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log.log', filemode='w'
                    )    

api_key = os.getenv('API_KEY')
db_user = os.getenv('POSTGRES_USER')
db_pw = os.getenv('POSTGRES_PASSWORD')
host = os.getenv('POSTGRES_HOST')
db = os.getenv('POSTGRES_DB')
#schema = os.getenv('SCHEMA')

# logging.info(f'env variables have been loaded. We are going to upload to {db}')



logging.info('creating db if not already created')
engine = create_engine(f"postgresql://{db_user}:{db_pw}@{host}:5432/{db}")
if not database_exists(engine.url):
    create_database(engine.url)

# define empty dictionary to put data into
exchange_dict = {'extracted_at':[],
                    'extracted_data':[]}


for day in pd.date_range(start='07/03/2023', end='07/04/2023', ):
    api_url = f"http://api.exchangeratesapi.io/v1/{str(day)[:-9]}?access_key={api_key}"
    response = requests.request("GET", api_url)
    logging.warning(f'attempt resulted in {response.status_code}')
    logging.warning('if not 200 -> research error')
    #print(response.status_code) # make sure you get a 200 repsonse
    # wrap response into dictionary
    exchange_dict['extracted_at'].append(datetime.datetime.now())
    exchange_dict['extracted_data'].append(json.loads(response.text))

# define data types for table in DB
dtype_dict = {'extracted_at':types.DateTime,
                    'extracted_data':postgres_json}

# convert dict to dataframe
exchange_df = pd.DataFrame(exchange_dict)

logging.info('attempting to load data to db')

# send df to DB
try:
    exchange_df.to_sql('raw_rates', engine, if_exists='replace', dtype=dtype_dict)
    logging.debug('db updated')
except ConnectionError:
    logging.error('connection not made')

logging.debug('data has been successfully loaded')