from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

wallets = {}

def get_or_create_wallet(user_id):
    if user_id not in wallets:
        wallets[user_id] = {
            "balance": 0,
            "created_at": datetime.now().isoformat(),
        }
    return wallets[user_id]

@app.route("/wallet")
def wallet():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400
    wallet = get_or_create_wallet(user_id)
    return jsonify(wallet)

if __name__ == "__main__":
    app.run()
