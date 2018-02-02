from ..base import Sendable


class Contact(Sendable):
    def __init__(self, tg, data):
        super().__init__(tg)
        self.phone_number = data['phone_number']
        self.first_name = data['first_name']
        self.last_name = data.get('last_name')
        self.user_id = data.get('user_id')

    def to_user(self):
        return self._tg.user(user_id=self.user_id)

    def __repr__(self):
        return '<User {}>'.format(self.phone_number)

    def __str__(self):
        if self.last_name:
            return '{} {}'.format(self.first_name, self.last_name)
        return self.first_name

    def send(self, chat, *args, **kwargs):
        chat = self._chat_parser(chat)
        return chat.send_contact(self, None, None, None, *args, **kwargs)
