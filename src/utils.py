import os
import sys

import numpy as np  
import pandas as pd
import dill
from src.exception import CustomException

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