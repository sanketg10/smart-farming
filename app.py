import numpy as np                      # To help us perform operations such as percentile
import pandas as pd                     # To help us read the csv and write to it
from pandas import Series, DataFrame    # To help us convert the read data to a DataFrame
import os.path                          # To check if a file already exists, if it does then create another one

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug="True",port=5002)