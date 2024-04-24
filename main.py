from flask import Flask, render_template, request, make_response, session
from typing import List
import random
import markdown
import asyncio
import datetime

from message_class import Message
from ai_g4f import ai_response

app = Flask(__name__)

# messages: List[Message] = [Message('user1', 'text-test'), Message('user2', 'text2-test')]
messages: List[Message] = []


@app.route('/', methods=['GET', 'POST'])
def get_chatroom():
    return render_template('chatroom.html')


@app.route('/postmessage', methods=['POST'])
async def post_message():
    if request.method == 'POST':
        text = request.json['message']
        r = make_response('Message accept!')
        r.headers['Content-Type'] = 'text/plain'
        messages.append(Message(username='user', text=request.json['message']))
        answer = await ai_response(text)
        html_text = markdown.markdown(answer)
        messages.append(Message(username='bot', text=html_text))
        # .....messages.append(Message(username='bot', text=request.json['message']))
        return {}


@app.route('/requestmessage', methods=['FETCH'])
async def request_message():
    st = datetime.datetime.now().timestamp()
    while len(messages) <= 0 or messages[-1].id <= request.json['last_message_id']:
        await asyncio.sleep(0.1)
        et = datetime.datetime.now().timestamp()
        if int(et - st) > 4:
            break
    msg = [m.to_dict() for m in messages if m.id > request.json['last_message_id']]
    # if random.random() > 0.5:
    #     messages.append(Message.generator_messages())
    if messages:
        del messages[0]
    return msg


if __name__ == '__main__':
    app.run(
        # debug=True,
        # threaded=True
    )
