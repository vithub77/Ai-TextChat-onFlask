from flask import Flask, render_template, request, make_response
from typing import List
import random

from message_class import Message

app = Flask(__name__)

messages: List[Message] = [Message('user1', 'text-test'), Message('user2', 'text2-test')]


@app.route('/', methods=['GET', 'POST'])
def get_chatroom():
    return render_template('chatroom.html')


@app.route('/postmessage', methods=['POST'])
def post_message():
    if request.method == 'POST':
        print(request.json['message'], 'request.get_json()')
        r = make_response('Message accept!')
        r.headers['Content-Type'] = 'text/plain'
        messages.append(Message(username='user', text=request.json['message']))
        # .....messages.append(Message(username='bot', text=request.json['message']))
        return {}


@app.route('/requestmessage', methods=['FETCH'])
def request_message():
    msg = [m.to_dict() for m in messages if m.id > request.json['last_message_id']]
    # if random.random() > 0.5:
    #     messages.append(Message.generator_messages())
    return msg

if __name__ == '__main__':
    app.run(debug=True)
