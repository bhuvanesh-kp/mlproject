from flask import Flask,render_template,request
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.exception import CustomException
from src.pipeline.predict_pipeline import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])
def predict_datapoint():
    try:
        if request.method == "GET":
            return render_template("home.html")
        
        else:
            data = Customdata(gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental level of education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test preparation course'),
            reading_score=int(request.form.get('writing score')),
            writing_score=int(request.form.get('reading score'))
            )

            pred = data.get_data_as_data_frame()
            print(pred)
            predict_pipeline = predictpipeline()
            results = predict_pipeline.predict(pred)
            print("after Prediction")
            return render_template('home.html',results=results[0])

        
    except Exception as e:
        raise CustomException(e,sys)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')