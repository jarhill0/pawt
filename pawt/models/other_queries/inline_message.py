from json import dumps

from ..base import PAWTBase
from ..message_specials import GameHighScore
from ...const import API_PATH


class InlineMessage(PAWTBase):
    def __init__(self, tg, inline_message_id):
        super().__init__(tg)

        self.id = inline_message_id

    def edit_text(self, text, parse_mode=None, disable_web_page_preview=None,
                  reply_markup=None):

        data = dict(inline_message_id=self.id)
        if reply_markup:
            data['reply_markup'] = dumps(reply_markup)  # yeah it's weird

        data['text'] = text
        if parse_mode:
            data['parse_mode'] = parse_mode
        if disable_web_page_preview:
            data['disable_web_page_preview'] = disable_web_page_preview
        return self._tg.post(API_PATH['edit_message_text'], data=data)

    def edit_caption(self, caption, reply_markup=None):
        data = dict(inline_message_id=self.id)
        if reply_markup:
            data['reply_markup'] = dumps(reply_markup)  # yeah it's weird

        data['caption'] = caption
        return self._tg.post(API_PATH['edit_message_caption'], data=data)

    def edit_reply_markup(self, reply_markup):
        data = dict(inline_message_id=self.id, reply_markup=dumps(reply_markup))
        return self._tg.post(API_PATH['edit_message_reply_markup'], data=data)

    def edit_live_location(self, latitude, longitude, reply_markup=None):
        info = dict(inline_message_id=self.id, latitude=latitude,
                    longitude=longitude)
        if reply_markup:
            info['reply_markup'] = dumps(reply_markup)
        return self._tg.post(API_PATH['edit_message_live_location'], data=info)

    def stop_live_location(self, reply_markup=None):
        info = dict(inline_message_id=self.id)
        if reply_markup:
            info['reply_markup'] = dumps(reply_markup)
        return self._tg.post(API_PATH['stop_message_live_location'], data=info)

    def get_game_high_scores(self, user):
        if not isinstance(user, (str, int)):
            user_id = user.id
        else:
            user_id = str(user)
        data = dict(inline_message_id=self.id, user_id=user_id)
        response = self._tg.post(API_PATH['get_game_high_scores'], data=data)
        return [GameHighScore(self._tg, data=ghs)
                for ghs in response]

    def set_game_score(self, user, score, force=False,
                       disable_edit_message=False):
        if not isinstance(user, (str, int)):
            user_id = user.id
        else:
            user_id = str(user)
        data = dict(inline_message_id=self.id, score=score, force=force,
                    disable_edit_message=disable_edit_message, user_id=user_id)
        return self._tg.post(API_PATH['set_game_score'], data=data)
