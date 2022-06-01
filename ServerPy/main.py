from flask import Flask, render_template, request, url_for, send_file, jsonify, make_response
import json
from flask_cors import CORS, cross_origin
from functionsdb import connectdbdel,connectdbdput,connectdbdpatch,connectdbget
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/users/get', methods=['GET'])
def getusers():
    a = connectdbget()
    response = make_response(jsonify(a))
    return response


@app.route('/users/del', methods=['DELETE'])
def delusers():
    username = request.args.get('username')
    connectdbdel(username)
    msg = 'deleted user' + username
    response = make_response(jsonify(msg))
    return response


@app.route('/users/put', methods=['PUT'])
def create():
    username= request.args.get('username')
    paswd = request.args.get('passwd')
    a = connectdbdput(username, paswd)
    msg = 'user created'
    response = make_response(jsonify(msg))
    return response


@app.route('/users/patch', methods=['PATCH'])
def update():
    username = request.args.get('username')
    paswd = request.args.get('passwd')
    a = connectdbdpatch(username, paswd)
    msg = 'passwd changed'
    response  = make_response(jsonify(msg))
    return response


if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)

