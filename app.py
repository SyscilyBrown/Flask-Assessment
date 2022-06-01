from flask import Flask, jsonify,request, render_template, redirect, session
from forex_python.converter import CurrencyRates, CurrencyCodes
from forex import list_of_conversions
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"

valid_conversions = list_of_conversions()
exchange_rate=CurrencyRates()
currency_codes = CurrencyCodes()

@app.route("/")
def homepage():
    print("ldjfasdkfjlsjfdl;sdfj")
    logging.info("ldasksdljfdls")
    return render_template("conversioninput.html")


@app.route("/conversionoutput")
def output():
    conversion_input = request.args["conversion_input"]
    conversion_output = request.args["conversion_output"]
    amount = float(request.args["amount"])
    results = str(round(exchange_rate.convert(conversion_input, conversion_output, amount),2))
    symbol=currency_codes.get_symbol(conversion_output)
    logging.info("lmadlfslfkdjsl")
    logging.info(results)
    print(results)
    print(exchange_rate.convert(conversion_input, conversion_output, amount))



    return render_template("conversionoutput.html", conversion_input = conversion_input,conversion_output = conversion_output, amount=amount, results=results)


