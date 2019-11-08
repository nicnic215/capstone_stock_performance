from flask import Flask, render_template, request, session, redirect
import numpy as np
import pandas as pd
from time import time

app=Flask(__name__)

df_full = pd.read_excel("./capstone_data/final_predicted_vs_actual.xlsx", index_col=[0,1], parse_dates=True)
df_full = df_full.reset_index()
df_full["date"] = df_full["date"].dt.to_period('M')
df_full = df_full.set_index(['date', 'STOCK_TICKER'])

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        input_month = request.form.get('month')
        s_ticker1 = request.form.get('ticker1')
        s_ticker2 = request.form.get('ticker2')
        s_ticker3 = request.form.get('ticker3')
        prediction1 = df_full.xs((input_month,s_ticker1))
        prediction1 = pd.DataFrame(prediction1)
        prediction2 = df_full.xs((input_month,s_ticker2))
        prediction2 = pd.DataFrame(prediction2)
        prediction3 = df_full.xs((input_month,s_ticker3))
        prediction3 = pd.DataFrame(prediction3)
        prediction_all = pd.concat([prediction1, prediction2, prediction3], axis=1, sort=False)
        prediction_all = [prediction_all.to_html(header="true", table_id="table")]
        return render_template("result.html", tables = prediction_all)

if __name__ == "__main__":
    app.run()