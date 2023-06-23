from flask import Flask, jsonify, request
import hashlib

app = Flask(__name__)

@app.route("/hashingmd5", methods = ['POST'])
def call_first_container():
    data = request.json
    file = data['file']
    checkSumResult = md5(file)
    return jsonify({"file" : file, "checksum" : checkSumResult})

def md5(fname):
    return hashlib.md5(open(fname,'rb').read()).hexdigest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

# References:
    # 1. https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file