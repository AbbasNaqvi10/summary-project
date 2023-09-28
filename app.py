from flask import Flask,request
import json
from utils import summerize_it
import time

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/get_summary",methods=['POST','GET'])
def summarize():
    start = time.time()
    if request.method == 'GET':
        return 'This is a post request 🤣'
    else:
        try:
            para = request.json["paragraph"]
            return {"Original Text":para,"summary": summerize_it(para),"response_time":round(time.time()- start,2)}
        except Exception as e:
            return {"error":str(e)}

if __name__ == '__main__':
    app.run(port=5000)