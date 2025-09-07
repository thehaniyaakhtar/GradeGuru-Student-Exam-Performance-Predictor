from flask import Flask, request, render_template
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Home page
@app.route('/')
def index():
    return render_template('home.html')

# Prediction route
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    try:
        # Collect all form inputs
        data = CustomData(
            Hours_Studied=float(request.form.get('Hours_Studied')),
            Attendance=float(request.form.get('Attendance')),
            Sleep_Hours=float(request.form.get('Sleep_Hours')),
            Previous_Scores=float(request.form.get('Previous_Scores')),
            Tutoring_Sessions=float(request.form.get('Tutoring_Sessions')),
            Physical_Activity=float(request.form.get('Physical_Activity')),
            Parental_Involvement=request.form.get('Parental_Involvement'),
            Access_to_Resources=request.form.get('Access_to_Resources'),
            Extracurricular_Activities=request.form.get('Extracurricular_Activities'),
            Motivation_Level=request.form.get('Motivation_Level'),
            Internet_Access=request.form.get('Internet_Access'),
            Family_Income=request.form.get('Family_Income'),
            Teacher_Quality=request.form.get('Teacher_Quality'),
            School_Type=request.form.get('School_Type'),
            Peer_Influence=request.form.get('Peer_Influence'),
            Learning_Disabilities=request.form.get('Learning_Disabilities'),
            Parental_Education_Level=request.form.get('Parental_Education_Level'),
            Distance_from_Home=request.form.get('Distance_from_Home'),
            Gender=request.form.get('Gender')
        )

        # Convert to DataFrame
        pred_df = data.get_data_as_data_frame()
        print("Input DataFrame:\n", pred_df)

        # Predict
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        try:
            score = float(results[0])
        except Exception:
            score = results[0]

        return render_template('home.html', results=round(score, 2) if isinstance(score, float) else score)

    except Exception as e:
        # Show the error in browser for debugging
        return f"Error occurred: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
