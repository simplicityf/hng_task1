from flask import Flask, jsonify
from flask_cors import CORS
import datetime
import requests


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    try: 
        # Return JSON response containing the GitHub URL, current datetime, and email
        respone_data = {
            "email": "omobolanlehazeezat@gmail.com", 
            "current_datetime": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "github_url": "https://github.com/simplicityf/hng_task1"
        }
        return jsonify(respone_data), 200
        
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()
