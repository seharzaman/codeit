#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the form data
    density = float(request.form['density'])
    age = float(request.form['age'])
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    # ... repeat for the rest of the input fields

    # Perform the prediction and classification logic here

    # Render the results template with the predicted values and classification

@app.route('/progress', methods=['POST'])
def progress():
    # Retrieve the progress data from the form fields
    # ... repeat for the rest of the input fields

    # Perform the progress evaluation logic here

    # Render the progress template with the evaluation result and plot

if __name__ == '__main__':
    app.run(debug=True)

