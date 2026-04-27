from flask import Flask, render_template, request , jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)

# model = pickle.load(open('scaler.pkl', 'rb')) 
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':

        Fuel_Type_Diesel = 0

        Year = int(request.form['Year'])
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Kms_Driven2 = np.log(Kms_Driven)
        Owner = int(request.form['Owner'])

        Fuel_Type_Petrol = request.form['Fuel_Type_Petrol']
        if Fuel_Type_Petrol == 'Petrol':
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0
        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 1

        Year = 2020 - Year

        prediction = [5.0]

        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text=f'Price: {output}')

    else:
        return "Please open home page"

if __name__=="__main__":
    app.run(debug=True)
