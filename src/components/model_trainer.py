import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import AdaBoostRegressor, BaggingRegressor, ExtraTreesRegressor, GradientBoostingRegressor, \
    RandomForestRegressor, StackingRegressor, VotingRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object
from src.utils import evaluate_model

from dataclasses import dataclass
import os
import sys


@dataclass
class ModelTrainingConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainingConfig()

    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info('Splitting dependent and independent variables from train and test data')
            X_train,y_train,X_test,y_test =(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            base_regressors = [
                ('rf', RandomForestRegressor(n_estimators=50, random_state=42)),
                ('gb', GradientBoostingRegressor(n_estimators=50, random_state=42)),
                ('svr', SVR())
                ]

            final_regressor = LinearRegression()

            models = {
                "Linear_model":LinearRegression(),
                "Lasso_model":Lasso(),
                "Ridge_model":Ridge(),
                "ElasticNet_model":ElasticNet(),
                "DecisionTreeRegressor":DecisionTreeRegressor(),
                "SVR":SVR(),
                "AdaBoostRegressor":AdaBoostRegressor(),
                "BaggingRegressor":BaggingRegressor(),
                "ExtraTreesRegressor":ExtraTreesRegressor(),
                "GradientBoostingRegressor":GradientBoostingRegressor(),
                "RandomForestRegressor":RandomForestRegressor(),
                "StackingRegressor":StackingRegressor(estimators=base_regressors, final_estimator=final_regressor),
                "VotingRegressor":VotingRegressor(estimators=base_regressors)
                 }
            
            
            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')

            # To get best model score from dictionary 
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')

            save_object(
                 file_path=self.model_trainer_config.trained_model_file_path,
                 obj=best_model
            )

        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise CustomException(e,sys)
        

