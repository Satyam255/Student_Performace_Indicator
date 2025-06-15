import os
import sys

import numpy as np  
import pandas as pd
import dill
from src.exception import CustomException
from sklearn.metrics import r2_score

def save_object(file_path,obj):
    """
    Saves an object to a specified file path using numpy's save function.
    
    Parameters:
    - file_path (str): The path where the object will be saved.
    - obj: The object to be saved.
    
    Raises:
    - CustomException: If there is an error during saving the object.
    """
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)  # Create directory if it doesn't exist
        with open (file_path, 'wb') as file_obj:
           dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys) 
    
def evaluate_models(X_train, y_train, X_test, y_test, models):
    """
    Evaluates multiple regression models and returns a report of their performance.
    
    Parameters:
    - X_train: Training feature set.
    - y_train: Training target variable.
    - X_test: Testing feature set.
    - y_test: Testing target variable.
    - models (dict): Dictionary of model names and their instances.
    
    Returns:
    - model_report (dict): Dictionary containing model names and their R2 scores.
    """
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            model.fit(X_train, y_train)
            y_train_pred = model.predict(X_train)
            train_model_score = r2_score(y_train, y_train_pred)
            y_test_pred = model.predict(X_test)
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score
        return report
    except Exception as e:
        raise CustomException(e, sys)