import random
import string


class Message:
    username = ''
    text = ''
    id = 0
    counter = 1

    def __init__(self, username, text):
        self.username = username
        self.text = text
        self.id = self.counter
        Message.counter += 1

    def to_dict(self):
        return {
            'username': self.username,
            'text': self.text,
            'id': self.id
        }

    @classmethod
    def generator_messages(cls):
        return Message(username=f'User:{random.randint(1, 1000)}',
                       text=' '.join(["".join(random.choices(string.ascii_lowercase, k=random.randint(1, 7)))
                                      for _ in range(random.randint(1, 4))]))
