from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Initialize Groq API settings
api_key = os.environ.get("GROQ_API_KEY", "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")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_answer(question: str) -> str:
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "llama3-8b-8192",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant powered by Llama 3. Answer questions accurately, concisely, and with relevant details."
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
        
        response = requests.post(GROQ_API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return str(e)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    question = data.get('message', '')
    
    if not question:
        return jsonify({"error": "No message provided"}), 400
    
    answer = generate_answer(question)
    return jsonify({"response": answer})

@app.route('/health')
def health():
    return "LLaMA QA API is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
