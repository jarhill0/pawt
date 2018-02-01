from .location import Location
from ..base import Sendable


class Venue(Sendable):
    def __init__(self, tg, data):
        super().__init__(tg)

        self.location = Location(tg, data=data['location'])
        self.title = data['title']
        self.address = data['address']
        self.foursquare_id = data.get('foursquare_id')

    def __repr__(self):
        return '<Venue {}>'.format(self.title)

    def __str__(self):
        return self.title

    def send(self, chat, *args, **kwargs):
        chat = self._chat_parser(chat)
        return chat.send_venue(self, None, None, None, None, None,
                               *args, **kwargs)
