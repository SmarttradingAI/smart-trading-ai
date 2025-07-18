from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # --- FAKE AI LOGIC ---
    if "bitcoin" in user_message.lower():
        reply = "Bitcoin is a decentralized digital currency."
    elif "forex" in user_message.lower():
        reply = "Forex stands for the foreign exchange market."
    elif "stock" in user_message.lower():
        reply = "Stocks represent ownership in a company."
    elif "hello" in user_message.lower() or "how are you" in user_message.lower():
        reply = "Hi there! How can I help you with trading today?"
    else:
        reply = "I'm still learning. Ask me about Bitcoin, forex, or stocks!"

    return jsonify({"reply": reply})
