from flask import Flask, render_template, request, jsonify
from typing import List

app = Flask(__name__)
message: List = []


@app.route('/', methods=['GET'])
def get_chatroom():
    return render_template('chatroom.html')


@app.route('/postmessage', methods=['POST'])
def post_message():
    pass


@app.route('/requestmessage', methods=['FETCH'])
def request_message():
    # return jsonify({'ping': 'pong'})
    return {'ping': 'pong'}


if __name__ == '__main__':
    app.run(debug=True)
