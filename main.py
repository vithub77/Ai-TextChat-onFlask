from flask import Flask, render_template, request
from typing import List
import random

from message_class import Message

app = Flask(__name__)

messages: List[Message] = [Message('user1', 'text-test'), Message('user2', 'text2-test')]


@app.route('/', methods=['GET'])
def get_chatroom():
    return render_template('chatroom.html')


@app.route('/postmessage', methods=['POST'])
def post_message():
    pass


@app.route('/requestmessage', methods=['FETCH'])
def request_message():
    msg = [m.to_dict() for m in messages if m.id > request.json['last_message_id']]
    if random.random() > 0.5:
        messages.append(Message.generator_messages())
    return msg

if __name__ == '__main__':
    app.run(debug=True)
