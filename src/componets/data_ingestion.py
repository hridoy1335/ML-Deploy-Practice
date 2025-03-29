import os
import sys
import pandas as pd
from src.logger import logging
from dataclasses import dataclass
from src.exception import CustomException
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw_data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:
            df = pd.read_csv(os.path.join('notebook/data/student_data.csv'))
            logging.info('Data ingestion started')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info('Raw data saved')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            logging.info('Train data saved')
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('Test data saved')
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
    print("Data ingestion completed successfully.")
# This code is a part of a data ingestion module that reads a CSV file containing student data,
# splits it into training and testing datasets, and saves them to specified paths.
# It uses the pandas library for data manipulation and sklearn for splitting the dataset.
# The code is structured using a class and a dataclass for configuration,
# and it includes logging for tracking the process.
# The code also handles exceptions using a custom exception class.
# The script can be run directly to execute the data ingestion process.
# It is assumed that the necessary directories and files are in place for the code to run successfully.
