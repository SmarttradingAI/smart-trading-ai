from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'response': '❌ Please type a message.'})
    
    try:
        # Call GPT API with dynamic prompt
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are SmartTradingAI. Detect the user's language and always reply in the same language. If the user asks about trading (buy/sell/hold), give meaningful but safe suggestions like 'This is not financial advice, but here’s what I suggest…'. If it's a general question, just answer helpfully."},
                {"role": "user", "content": user_message}
            ]
        )
        ai_reply = response.choices[0].message.content.strip()
        return jsonify({'response': ai_reply})
    
    except Exception as e:
        return jsonify({'response': f'❌ Error: {str(e)}'})

# Render compatibility
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
