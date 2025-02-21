from flask import Flask, request
from execute_trade import place_order

app = Flask(__name__)

@app.route("/trade", methods=["POST"])
def trade():
    data = request.json
    symbol = data["symbol"]
    side = data["side"]
    amount = data["amount"]
    place_order(symbol, side, amount)
    return {"status": "Order placed!"}

if __name__ == "__main__":
    app.run(debug=True)
