import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd



class PredictPipeline:

    def __init__(self):
        pass

    def predict(self,features):

        try:
            preprocessor_path = os.path.join('artifacts','preprocessor.pkl')
            model_path = os.path.join('artifacts','model.pkl')

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(features)
            
            pred = model.predict(data_scaled)

            return pred
            
        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)

class CustomData:

    def __init__(self,Median_Sale_Price_House:float,Personal_Income_Per_Capita:float,Property_Tax:float,
                Nasdaqcom:float,Construction_Employment_Cost:float,Population:float,
                New_House_Units_Construction:float, CPI:float, Mortage_Rate:float,
                Unemployment_Rate:float, Household_Debt_Payment:float, Recession_Rate:float,
                Date_Quarter:int,Date_Year:int):
        
        self.Median_Sale_Price_House = Median_Sale_Price_House
        self.Personal_Income_Per_Capita = Personal_Income_Per_Capita
        self.Property_Tax = Property_Tax
        self.Nasdaqcom = Nasdaqcom
        self.Construction_Employment_Cost = Construction_Employment_Cost
        self.Population = Population
        self.New_House_Units_Construction = New_House_Units_Construction
        self.CPI = CPI
        self.Mortage_Rate = Mortage_Rate
        self.Unemployment_Rate = Unemployment_Rate
        self.Household_Debt_Payment = Household_Debt_Payment
        self.Recession_Rate = Recession_Rate
        self.Date_Quarter = Date_Quarter
        self.Date_Year = Date_Year
       



    def get_data_as_dataframe(self):
        
        try:
            custom_data_input_dict = {
                'Median_Sale_Price_House':[self.Median_Sale_Price_House],
                'Personal_Income_Per_Capita':[self.Personal_Income_Per_Capita],
                'Property_Tax':[self.Property_Tax],
                'Nasdaqcom':[self.Nasdaqcom],
                'Construction_Employment_Cost':[self.Construction_Employment_Cost],
                'Population':[self.Population],
                'New_House_Units_Construction':[self.New_House_Units_Construction],
                'CPI':[self.CPI],
                'Mortage_Rate':[self.Mortage_Rate],
                'Unemployment_Rate':[self.Unemployment_Rate],
                'Household_Debt_Payment':[self.Household_Debt_Payment],
                'Recession_Rate':[self.Recession_Rate],
                'Date_Quarter':[self.Date_Quarter],
                'Date_Year':[self.Date_Year]

            }

            df = pd.DataFrame(custom_data_input_dict)
            logging.info("Dataframe Gathered")
            return df
        
        except Exception as e:
            logging.info("Exception occured in get_data_as_dataframe function")
            raise CustomException(e,sys)
