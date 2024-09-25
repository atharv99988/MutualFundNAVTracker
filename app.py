from flask import Flask
from controller import addNAVs

app = Flask(__name__)
addNAVs.getMutualFund()

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    # Set a custom port, e.g., port 8080
    app.run(debug=False, port=8080)
