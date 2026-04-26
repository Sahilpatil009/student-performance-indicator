import os
import sys
import dill

from src.exception import CustomException


def save_object(file_path: str, obj) -> None:
    try:
        # Extract directory path
        dir_path = os.path.dirname(file_path)

        # Create directory only if it exists in path
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        # Save object using dill
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)