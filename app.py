from flask import (
    Flask, 
    jsonify, 
    render_template, 
    request, 
    redirect)
import json
import pandas as pd 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")
#Set Squalchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/CryptoData.sqlite'
#make a db reference
db = SQLAlchemy(app)

#create a empty database Model of USD/BTC
class CryptoData(db.Model):
    __tablename__ = 'CryptoTable'

    id = db.Column(db.Integer, primary_key=True)
    # Currency = db.Column(db.String(64))
    Date = db.Column(db.String(64))
    Close = db.Column(db.Integer)

    def __repr__(self):
        return '<CryptoData %r>' % (self.Currency)
    # CryptoData.query.all()

# #Create database tables
@app.before_first_request
def setup():
#     Recreate database each time for demo
#     db.drop_all()
    db.create_all()

file = "static/data/historical_data_final.csv"
historical_df = pd.read_csv(file)

currency_list = {
        "XRP" : 1,
        "ETH" : 2, 
        "LTC" : 3, 
        "BCC" : 4, 
        "EOS" : 5, 
        "BNC" : 6
        }   


currency_explore = {
        "XRPBTC" : 1,
        "ETHBTC" : 2, 
        "LTCBTC" : 3, 
        "BCCBTC" : 4, 
        "EOSBTC" : 5, 
        "BNCBTC" : 6
        }  

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/explore")
def explore():
    return render_template('explore.html')
    
@app.route("/history")
def history():
    return render_template('history.html')

@app.route("/comparison")
def comparison():
    return render_template('comparison.html')

'''
The following routes are for calling the historical data API 
of each ETC and plotting the data in JS.
'''
@app.route("/BTC_explore")
def btc_explore():
     return (jsonify(list(currency_explore)))

@app.route("/BTC")
def names():
    return (jsonify(list(currency_list)))
    
@app.route("/historical_data/<correctedCurrency>")
def historical_data(correctedCurrency):
    currency_data = historical_df.loc[historical_df["correctedCurrency"] == correctedCurrency]

    data = {
        "Date": currency_data["Date"].tolist(),
        "Close": currency_data["Close"].tolist(),
    }

    return jsonify(data)
#put flask data into element "plot"
# Query the database and send the jsonified results
@app.route("/plot_USDBTC")
def USDBTC_data():
    # print("hello")
    #Query for the USDBTC data using pandas
    results = db.session.query(CryptoData.Date, CryptoData.Close).order_by(CryptoData.Date.desc()).all()
    # print(results)
    Date = [result[0] for result in results]
    Price = [result[1] for result in results]
    # print(Date, Price)

#(change array to list and set the x and y data)

#Directory change into plot trace
    trace = {
        "x": Date,
        "y": Price,
        "type": "plot"
    }

    return jsonify(trace)


if __name__ == "__main__":
    app.run(debug=True)
