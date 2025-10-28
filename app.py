import pickle
from flask import request, Flask, render_template, redirect, url_for, flash
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd




# ======================================Create app=================================================
app = Flask(__name__)


# routes===================================================================

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def home():
    return render_template("index.html")
@app.route('/job')
def job():
    return render_template('job.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')





# ========================python main===================================================
if __name__ == "__main__":
    app.run(debug=True)