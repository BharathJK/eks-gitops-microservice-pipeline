from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "production-api",
        "environment": os.getenv("APP_ENV", "production")
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
