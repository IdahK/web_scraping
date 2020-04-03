from flask import Flask,jsonify
from scraping import scrape

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(Elements = scrape())
 
#app.run(debug=True)
if __name__ == "__main__":
    app.run(debug = True)    















