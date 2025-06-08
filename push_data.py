import os
import sys
import json

from dotenv import load_dotenv
import certifi
import pandas as pd 
import numpy as np 
import pymongo
import pymongo.message
import pymongo.mongo_client
from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logging.logger import logging
load_dotenv()
ca = certifi.where()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def csv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_to_mongodb(self,records,database,collection):
        try:
            self.records = records
            self.database = database
            self.collection = collection
            
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            
            self.collection.insert_many(self.records)
            return(len(records))
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__ == '__main__':
    FILE_PATH = 'Network_Data\phisingData.csv'
    DATABASE = 'RushiAI'
    Collection = 'NetworkData'
    obj = NetworkDataExtract()
    records = obj.csv_to_json_converter(file_path=FILE_PATH)
    no_of_records = obj.insert_data_to_mongodb(records,DATABASE,Collection)
    print(no_of_records)
    