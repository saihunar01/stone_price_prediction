import os
import sys
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from src.logger import logging
from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open (file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)

def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        report={}

        for i in range(len(list(models))):
            model=list(models.values())[i]
            # Train model
            model.fit(X_train,y_train)

                    
            #Make Predictions for testing data
            y_test_pred=model.predict(X_test)

            #Get r2 Score for train and test data
            
            test_model_score=r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]]=test_model_score

        return report
   
    except Exception as e:
        logging.info('Exception occured in Model Training')
        raise CustomException (e,sys)


def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e: 
        logging.info('Exception occured at loading the object in utils file')
        raise CustomException(e,sys)
