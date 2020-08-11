from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
model = pickle.load(open("ym.pickle", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("deploy.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":



        MONTH = float(request.form["MONTH"])
        DAY = float(request.form["DAY"])
        DAY_OF_WEEK = float(request.form["DAY_OF_WEEK"])
        AIRLINE = float(request.form["AIRLINE"])
        SCHEDULED_DEPARTURE = float(request.form["SCHEDULED_DEPARTURE"])
        DEPARTURE_TIME = float(request.form["DEPARTURE_TIME"])
        SCHEDULED_TIME = float(request.form["SCHEDULED_TIME"])
        DISTANCE = float(request.form["DISTANCE"])
        ARIVAL_TIME = float(request.form["ARIVAL_TIME"])
        SCHEDULED_ARRIVAL = float(request.form["SCHEDULED_ARRIVAL"])
        ARRIVAL_DELAY = float(request.form["ARRIVAL_DELAY"])

        features = np.array([[MONTH,DAY,DAY_OF_WEEK,AIRLINE,SCHEDULED_DEPARTURE,DEPARTURE_TIME,
                        SCHEDULED_TIME,DISTANCE,ARIVAL_TIME,SCHEDULED_ARRIVAL,ARRIVAL_DELAY]])


        prediction=model.predict(features)


        output=round(prediction[0],2)

        return render_template('deploy.html',prediction_text="Predicted Airline Delay in min. {}" .format(output))


    return render_template("deploy.html")



if __name__ == "__main__":
    app.run(debug=True)
