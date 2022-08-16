import requests
from flask import Flask
print('Hallo world')
print(1+1)
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()