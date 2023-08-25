from decimal import Decimal, ROUND_HALF_UP
from flask import Flask, request, jsonify
from config import exchange_rates
app = Flask(__name__)


def convert_currency(amount, from_currency,  to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return None

    rate = exchange_rates[from_currency][to_currency]
    converted_amount = Decimal(amount) * Decimal(rate)
    return converted_amount


def error_response(message):
    return jsonify({"msg": "fail", "error": message}), 400


def validate_amount(amount_str):
    try:
        amount = Decimal(amount_str.replace('$', '').replace(',', ''))
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return amount
    except ValueError:
        return None


@app.route("/")
def home():
    return "Hello, This is a Exchange rates api"


@app.route('/convert', methods=['GET'])
def currency_converter():
    source_currency = request.args.get('source', '').upper()
    target_currency = request.args.get('target', '').upper()
    if not source_currency or not target_currency:
        return error_response("Missing source or target currency")

    amount_str = request.args.get('amount', '')
    if not amount_str:
        return error_response("Missing 'amount' parameter")

    amount = validate_amount(amount_str)
    if amount is None:
        return error_response("Invalid amount")

    converted_amount = convert_currency(
        amount, source_currency, target_currency)
    if converted_amount is None:
        return error_response("Invalid currency")

    formatted_amount = "${:,.2f}".format(converted_amount)
    return jsonify({"msg": "success", "amount": formatted_amount})


if __name__ == '__main__':
    app.run()
