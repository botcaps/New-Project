import sys
import os
# Add the src directory to the Python path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from Newproject.logger import logging
from Newproject.exception import customException
from Newproject.components.data_ingestion import DataIngestion
from Newproject.components.data_ingestion import DataIngestionConfig
from Newproject.components.data_transformation import DataTransformationConfig,DataTransformation

import sys




if __name__=="__main__":
    logging.info("The execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)

        
    except Exception as e:
        logging.info("Custom Exception")
        raise customException(e,sys)
