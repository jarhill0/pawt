from ..base import PAWTBase
from ..message import Message
from ..other_queries import inline_message as im_mod
from ..user import User
from ...const import API_PATH


class CallbackQuery(PAWTBase):
    def __init__(self, tg, data):
        super().__init__(tg)

        self.id = data['id']
        self.user = User(data['from'])
        self.from_ = self.user
        self.message = None
        self.inline_message = None
        self.chat_instance = data['chat_instance']
        self.data = data.get('data')
        self.game_short_name = data.get('game_short_name')

        if data.get('message'):
            self.message = Message(tg, data['message'])
        if data.get('inline_message_id'):
            self.inline_message = im_mod.InlineMessage(tg,
                                                       data[
                                                           'inline_message_id'])

    def __repr__(self):
        return '<CallbackQuery {}>'.format(self.id)

    def answer(self, text=None, show_alert=False, url=None, cache_time=None):
        data = dict(callback_query_id=self.id)
        if text:
            data['text'] = text
        if show_alert:
            data['show_alert'] = show_alert
        if url:
            data['url'] = url
        if cache_time:
            data['cache_time'] = cache_time
        return self._tg.post(API_PATH['answer_callback_query'], data=data)
