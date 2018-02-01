from .base import Sendable
from .message_specials import FileWrapper
from ..const import API_PATH
from ..models import mask_position, photo_size, sticker_set as ss_mod, \
    user as user_mod


class Sticker(FileWrapper, Sendable):
    # rewrote this class and I'm positive it broke things. Meh.
    def __init__(self, tg, data):
        super().__init__(tg, data)

        self.width = data['width']
        self.height = data['height']
        self.emoji = data.get('emoji')
        self.set_name = data.get('set_name')

        if data.get('thumb'):
            self.thumb = photo_size.PhotoSize(tg, data['thumb'])
        else:
            self.thumb = None
        if data.get('mask_position'):
            self.mask_position = mask_position.MaskPosition(data['mask_pos'])
        else:
            self.mask_position = None

    def add_to_set(self, user, set_):
        if not isinstance(user, user_mod.User):
            user = user_mod.User(self._tg, user_id=user)
        if isinstance(set_, ss_mod.StickerSet):
            name = set_.name
        else:
            name = str(set_)
        return user.add_sticker_to_set(name, self, self.emoji,
                                       self.mask_position)

    def delete(self):
        return self._tg.get(API_PATH['delete_sticker_from_set'],
                            data={'sticker': self.file.id})

    def get_set(self):
        return self._tg.sticker_set(self.set_name)

    def set_position(self, position):
        return self._tg.get(API_PATH['set_sticker_position_in_set'],
                            data=dict(sticker=self.file.id,
                                      position=position))

    def send(self, chat, *args, **kwargs):
        chat = self._chat_parser(chat)
        return chat.send_sticker(self, *args, **kwargs)
