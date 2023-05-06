# stores the list
from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def crypto_info():
    print("Request received... getting data.")
    response = requests.get('http://api.coincap.io/v2/assets')
    print("Sending data to client.")
    return response.json()

if __name__ == '__main__':
    app.run(port=3000)
