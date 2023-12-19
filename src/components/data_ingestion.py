from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import pandas as pd
import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import *

@dataclass
class DataIngestionConfig():
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','data.csv')


class DataIngestion():
    def __init__(self):
        self.ingestion_congif = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Entered data ingestion method')
        try:
            df = pd.read_csv("notebook\data\stud.csv\Stud.csv")
            logging.info('Reading data from dataframe')
            os.makedirs(os.path.dirname(self.ingestion_congif.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_congif.raw_data_path,index=False,header=True)
            logging.info('train test has been initialized ')
            train_set , test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_congif.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_congif.test_data_path,index=False,header=True)
            logging.info('Ingestion of data is complete')

            return (
                self.ingestion_congif.train_data_path,
                self.ingestion_congif.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        


if __name__ == '__main__':
    obj = DataIngestion()
    train_set,test_set = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_set,test_set)