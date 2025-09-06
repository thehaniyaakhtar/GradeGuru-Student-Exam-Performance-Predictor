import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OrdinalEncoder

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
        
    def get_data_transformer_object(self):
        try:
            numerical_col = ['Hours_Studied', 
                             'Attendance', 
                             'Sleep_Hours', 
                             'Previous_Scores', 
                             'Tutoring_Sessions', 
                             'Physical_Activity'
            ]
                
            
            
            categorical_cols = ['Parental_Involvement', 
                                'Access_to_Resources', 
                                'Extracurricular_Activities', 
                                'Motivation_Level', 
                                'Internet_Access', 
                                'Family_Income', 
                                'Teacher_Quality', 
                                'School_Type', 
                                'Peer_Influence', 
                                'Learning_Disabilities', 
                                'Parental_Education_Level', 
                                'Distance_from_Home', 
                                'Gender'
            ]
            
            num_pipeline = Pipeline(
                steps = [
                    ("Imputer", SimpleImputer(strategy="median")),
                    ("scalar", StandardScaler())
                ]
            )
            
            cat_pipeline = Pipeline(
                
                steps=[
                    ("Imputer", SimpleImputer(strategy="most_frequent")),
                    ("Label_Encoder", OrdinalEncoder()),
                    ("scalar", StandardScaler())
                ]
            )
            
            logging.info(f"Categorical columns: {categorical_cols}")
            logging.info(f"Numerical columns: {numerical_col}")
            
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_col),
                    ("cat_pipelines", cat_pipeline, categorical_cols)
                ]
            )
            
            return preprocessor
            
        except Exception as e:
            raise CustomException(e, sys)
    
    def initiate_data_transform(self, train_path, test_path):
        
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info("Read train and test data completed")
            
            logging.info("Obtaining processing object")
            
            preprocessing_obj = self.get_data_transformer_object()
            
            target_column_name = "Exam_Score"
            numerical_col = ['Hours_Studied', 'Attendance', 'Sleep_Hours', 'Previous_Scores', 'Tutoring_Sessions', 'Physical_Activity']
            
            input_feature_train_df = train_df.drop(columns = [target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]
            
            input_feature_test_df = test_df.drop(columns=[target_column_name], axis = 1)
            target_feature_test_df = test_df[target_column_name]
            
            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )
            
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)
            
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
        
            