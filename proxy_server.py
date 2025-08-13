from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BOT_SERVER_URL = "http://localhost:8000/relayExchangeResponse"
API_KEY = "Vibe-Nice-testing-PJA-200189"

@app.route("/", methods=["POST"])
def proxy():
    incoming_data = request.get_json()
    headers = {
        "Content-Type": "application/json",
        "X-Platform-API-Key": API_KEY
    }

    try:
        response = requests.post(BOT_SERVER_URL, json=incoming_data, headers=headers, timeout=10)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "Proxy is running"}), 200

if __name__ == "__main__":
    app.run(port=8080)
