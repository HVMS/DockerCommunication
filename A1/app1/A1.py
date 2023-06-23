from flask import Flask, request, jsonify
import os, requests, json

app = Flask(__name__)

@app.route('/checksum',methods = ['POST'])
def index():
    data = request.json
    for key, value in data.items():
        key1 = key
        value1 = value
    print(key1,value1)
    try:
        if data['file'] is None:
            raise KeyError
        elif key1 is not None and not os.path.exists(value1):
            return jsonify({"file": value1, "error" : "File not found."})
        elif key1 is None:
            return jsonify({"file": None, "error" : "Invalid JSON input."})
        else:
            file = data['file']
            final_data = sendToSecondContainer(file)
            return json.loads(final_data)
    except KeyError:
        return jsonify({"file": None, "error" : "Invalid JSON input."})
    
def sendToSecondContainer(fname):
    url = "http://app2:5001/hashingmd5"
    r = requests.post(url, json = {"file":fname})
    if r.ok:
        return r.text
    else:
        return "failed"

app.run(host='0.0.0.0', port=5000)

# References:
    # 1. https://stackoverflow.com/questions/9733638/how-to-post-json-data-with-python-requests