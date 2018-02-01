from ..base import Sendable


class Location(Sendable):
    def __init__(self, tg, data):
        super().__init__(tg)

        self.longitude = data['longitude']
        self.latitude = data['latitude']

    def __repr__(self):
        return '<Location {}>'.format(str(self))

    def __str__(self):
        return str((self.latitude, self.longitude))

    def send(self, chat, *args, **kwargs):
        chat = self._chat_parser(chat)
        return chat.send_location(self, None, None, *args, **kwargs)
