import flask
from flask import render_template
import pickle

import numpy as np
import pandas as pd

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import Model
from keras.models import Sequential
from keras.layers import Dense, Input

app = flask.Flask(__name__, template_folder = 'templates')

@app.route('/', methods = ['POST', 'GET'])

@app.route('/index', methods = ['POST', 'GET'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html')
    
    if flask.request.method == 'POST':
        # загружаем модель
        with open('Model/nl_model.pkl', 'rb') as f:
            loaded_model = pickle.load(f)

        # загружаем переменные
        # IW
        IW = float(flask.request.form['IW'])
        # IF
        IF = float(flask.request.form['IF'])
        # VW
        VW = float(flask.request.form['VW'])
        # FP
        FP = float(flask.request.form['FP'])
        # Depth
        Depth = float(flask.request.form['Depth'])
        # соберем все в строку DataFrame
        row = [IW, IF, VW, FP, Depth]
        cols = ['IW', 'IF', 'VW', 'FP', 'Depth']
        entry = pd.DataFrame(row, columns = cols)
        Width = loaded_model.predict(entry)

        return render_template('main.html', result = Width)
    
if __name__ == '__main__':
    app.run()