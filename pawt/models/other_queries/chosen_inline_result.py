from ..base import PAWTBase
from ..message_specials import Location
from ..other_queries import inline_message as im
from ..user import User


class ChosenInlineResult(PAWTBase):
    def __init__(self, tg, data):
        super().__init__(tg)
        self.id = data['result_id']
        self.result_id = data['result_id']
        self.user = User(data['from'])
        self.from_ = self.user
        self.location = None
        self.inline_message = None
        self.query = data['query']

        if data.get('location'):
            self.location = Location(self._tg, data['location'])
        if data.get('inline_message_id'):
            self.inline_message = im.InlineMessage(tg,
                                                   data['inline_message_id'])

    def __repr__(self):
        return '<ChosenInlineResult {}>'.format(self.id)
