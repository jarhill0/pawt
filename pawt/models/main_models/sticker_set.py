from ..base import PAWTLazy
from ...const import API_PATH
from ...exceptions import BadArgument


class StickerSet(PAWTLazy):
    def __init__(self, tg, name=None, data=None):
        super().__init__(tg)

        if bool(name) == bool(data):
            raise BadArgument('Exactly one of name and data must be given')

        self._fetched = bool(data)

        if name:
            self.name = name
        if data:
            self._set_known_attrs(data)

    def __eq__(self, other):
        return hasattr(other, 'name') and self.name == other.name

    def _load(self):
        d = self._tg.get(API_PATH['get_sticker_set'],
                         params=dict(name=self.name))
        self._set_known_attrs(d)

    def _set_known_attrs(self, data):
        self.name = data['name']
        self.title = data['title']
        self.contains_masks = data['contains_masks']
        self.stickers = [self._tg.sticker(data=o) for o in data['stickers']]

    def __repr__(self):
        return '<StickerSet {}>'.format(self.name)

    def __str__(self):
        return self.title

    def add(self, user, png_sticker, emojis, mask_position=None):
        if isinstance(user, (int, str)):
            user = self._tg.user(user_id=user)
        return user.add_sticker_to_set(self.name, png_sticker, emojis,
                                       mask_position)

    def set_chat_sticker_set(self, chat):
        if not hasattr(chat, 'set_sticker_set'):
            chat = self._tg.chat(chat)
        return chat.set_sticker_set(self)
