import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features: pd.DataFrame):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")

            # Reorder features according to preprocessor
            expected_features = preprocessor.feature_names_in_
            print("Incoming features:", list(features.columns))
            print("Preprocessor expects:", list(expected_features))

            # Reorder columns to match training
            features = features[expected_features]
            print("Reordered features:", list(features.columns))
            print("Shape of incoming:", features.shape)

            # Transform and predict
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 Hours_Studied: float,
                 Attendance: float,
                 Sleep_Hours: float,
                 Previous_Scores: float,
                 Tutoring_Sessions: float,
                 Physical_Activity: float,
                 Parental_Involvement: str,
                 Access_to_Resources: str,
                 Extracurricular_Activities: str,
                 Motivation_Level: str,
                 Internet_Access: str,
                 Family_Income: str,
                 Teacher_Quality: str,
                 School_Type: str,
                 Peer_Influence: str,
                 Learning_Disabilities: str,
                 Parental_Education_Level: str,
                 Distance_from_Home: str,
                 Gender: str):

        # Numerical
        self.Hours_Studied = Hours_Studied
        self.Attendance = Attendance
        self.Sleep_Hours = Sleep_Hours
        self.Previous_Scores = Previous_Scores
        self.Tutoring_Sessions = Tutoring_Sessions
        self.Physical_Activity = Physical_Activity

        # Categorical
        self.Parental_Involvement = Parental_Involvement
        self.Access_to_Resources = Access_to_Resources
        self.Extracurricular_Activities = Extracurricular_Activities
        self.Motivation_Level = Motivation_Level
        self.Internet_Access = Internet_Access
        self.Family_Income = Family_Income
        self.Teacher_Quality = Teacher_Quality
        self.School_Type = School_Type
        self.Peer_Influence = Peer_Influence
        self.Learning_Disabilities = Learning_Disabilities
        self.Parental_Education_Level = Parental_Education_Level
        self.Distance_from_Home = Distance_from_Home
        self.Gender = Gender

    def get_data_as_data_frame(self):
        try:
            data_dict = {
                "Hours_Studied": [self.Hours_Studied],
                "Attendance": [self.Attendance],
                "Sleep_Hours": [self.Sleep_Hours],
                "Previous_Scores": [self.Previous_Scores],
                "Tutoring_Sessions": [self.Tutoring_Sessions],
                "Physical_Activity": [self.Physical_Activity],
                "Parental_Involvement": [self.Parental_Involvement],
                "Access_to_Resources": [self.Access_to_Resources],
                "Extracurricular_Activities": [self.Extracurricular_Activities],
                "Motivation_Level": [self.Motivation_Level],
                "Internet_Access": [self.Internet_Access],
                "Family_Income": [self.Family_Income],
                "Teacher_Quality": [self.Teacher_Quality],
                "School_Type": [self.School_Type],
                "Peer_Influence": [self.Peer_Influence],
                "Learning_Disabilities": [self.Learning_Disabilities],
                "Parental_Education_Level": [self.Parental_Education_Level],
                "Distance_from_Home": [self.Distance_from_Home],
                "Gender": [self.Gender],
            }
            df = pd.DataFrame(data_dict)
            print("Input DataFrame:\n", df)
            return df

        except Exception as e:
            raise CustomException(e, sys)
