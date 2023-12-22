import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from src.exception import CustomException
from src.logger import logging
import os
from src.utils import save_object

from src.components.data_ingestion import DataIngestion


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            logging.info('Data Transformation initiated')
            numerical_cols = ['Median_Sale_Price_House', 'Personal_Income_Per_Capita', 'Property_Tax',
                                 'Nasdaqcom', 'Construction_Employment_Cost', 'Population',
                                 'New_House_Units_Construction', 'CPI', 'Mortage_Rate',
                                 'Unemployment_Rate', 'Household_Debt_Payment', 'Recession_Rate',
                                 'Date_Quarter', 'Date_Year']

            logging.info('Pipeline initiated')

            ##Numerical Pipeline
            num_pipeline = Pipeline(
                steps = [
                    ('imputer', SimpleImputer(strategy = 'median')),
                    ('scaler',StandardScaler())
                ]
        
            )

            preprocessor = ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_cols)
            ])

            logging.info("Pipeline completed")

            return preprocessor


        except Exception as e:
            logging.info('Error in Data Transformation')
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            ## Reading train and test data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Read train and test data completed')
            logging.info(f'Train Datafram Head : \n {train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head :\n {test_df.head().to_string()}')

            logging.info('Obtaining preprocessor object')
            preprocessor_obj = self.get_data_transformation_object()
            
            target = 'S&PCase_Schiller_Index'
            drop_columns = ['DATE',target]

            train_df.dropna(inplace = True)
            test_df.dropna(inplace = True)

            train_df["DATE"] = pd.to_datetime(train_df['DATE'])
            test_df["DATE"] = pd.to_datetime(test_df['DATE'])

            object_columns = [col for col in train_df.columns if train_df[col].dtype == 'O']

            for col in object_columns:
                train_df[col] = pd.to_numeric(train_df[col])
                train_df[col] = train_df[col].round(2)
                test_df[col] = pd.to_numeric(test_df[col])
                test_df[col] = test_df[col].round(2)

            numerical_columns = [col for col in train_df.columns if train_df[col].dtype == 'float64']
            for col in numerical_columns:
                train_df[col] = train_df[col].round(2)
                test_df[col] = test_df[col].round(2)
            
            train_df['Date_Quarter'] = train_df['DATE'].dt.quarter
            test_df['Date_Quarter'] = test_df['DATE'].dt.quarter

            train_df['Date_Year'] = train_df['DATE'].dt.year
            test_df['Date_Year'] = test_df['DATE'].dt.year


            input_feature_train_df = train_df.drop(columns =drop_columns)
            target_feature_train_df = train_df[target]

            input_feature_test_df = test_df.drop(columns = drop_columns)
            target_feature_test_df = test_df[target]

            ## Transforming using preprocessor obj
            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)

            logging.info('Applying preprocessing object on training and testing datasets')

            train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(

                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessor_obj
            )
            logging.info('Preprocessor pickle file saved')

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            logging.info('Exception occured in the initial_data_transformation ')
            raise CustomException(e,sys)
        

# if __name__=='__main__':
        
#         obj = DataIngestion()
#         train_path,test_path = obj.initiate_data_ingestion()
#         dt = DataTransformation()
#         dt.initiate_data_transformation(train_path,test_path )