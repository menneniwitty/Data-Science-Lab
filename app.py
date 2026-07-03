from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import os
import joblib
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
MODEL_FILE="model.pkl"
DATA_FILE="house_data.csv"

def train_model():
    data=pd.read_csv(DATA_FILE)
    X=data[["area","bedrooms","bathrooms","stories","parking","mainroad","guestroom","basement","hotwaterheating","airconditioning","prefarea","furnishingstatus"]]
    y=data["price"]
    model=LinearRegression()
    model.fit(X,y)
    joblib.dump(model,MODEL_FILE)
    return model

model=joblib.load(MODEL_FILE) if os.path.exists(MODEL_FILE) else train_model()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    vals=[float(request.form["area"]),int(request.form["bedrooms"]),int(request.form["bathrooms"]),int(request.form["stories"]),int(request.form["parking"]),int(request.form["mainroad"]),int(request.form["guestroom"]),int(request.form["basement"]),int(request.form["hotwaterheating"]),int(request.form["airconditioning"]),int(request.form["prefarea"]),int(request.form["furnishingstatus"])]
    pred=model.predict(np.array([vals]))[0]
    return render_template("index.html",prediction_text=f"Estimated House Price: ₹ {pred:,.2f}")

if __name__=="__main__":
    app.run(debug=True)
