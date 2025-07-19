from openai import OpenAI

client = OpenAI(api_key=openai_api_key)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({'response': "❌ Please type a message."})

    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        ai_reply = completion.choices[0].message.content
        return jsonify({'response': ai_reply})

    except Exception as e:
        return jsonify({'response': f"❌ Error: {str(e)}"})
