from ..base import PAWTBase, Sendable
from ..message_specials import FileWrapper
from ...const import API_PATH
from ...exceptions import BadArgument


class Sticker(FileWrapper, Sendable):
    # rewrote this class and I'm positive it broke things. Meh.
    def __init__(self, tg, data):
        super().__init__(tg, data)

        self.width = data['width']
        self.height = data['height']
        self.emoji = data.get('emoji')
        self.set_name = data.get('set_name')

        if data.get('thumb'):
            self.thumb = tg.photo_size(data=data['thumb'])
        else:
            self.thumb = None
        if data.get('mask_position'):
            self.mask_position = MaskPosition(data['mask_position'])
        else:
            self.mask_position = None

    def add_to_set(self, user, set_):
        if isinstance(user, (int, str)):
            user = self._tg.user(user_id=user)
        if not isinstance(set_, (int, str)):
            name = set_.name
        else:
            name = str(set_)
        return user.add_sticker_to_set(name, self, self.emoji,
                                       self.mask_position)

    def delete(self):
        return self._tg.get(API_PATH['delete_sticker_from_set'],
                            params={'sticker': self.file.id})

    def get_set(self):
        return self._tg.sticker_set(self.set_name)

    def set_position(self, position):
        return self._tg.get(API_PATH['set_sticker_position_in_set'],
                            params=dict(sticker=self.file.id,
                                        position=position))

    def send(self, chat, *args, **kwargs):
        chat = self._chat_parser(chat)
        return chat.send_sticker(self, *args, **kwargs)


class MaskPosition(PAWTBase):
    def __init__(self, data):
        super().__init__(tg=None)

        self.point = data['point']
        self.x_shift = data['x_shift']
        self.y_shift = data['y_shift']
        self.scale = data['scale']

        if self.point not in ("forehead", "eyes", "mouth", "chin"):
            raise BadArgument('Point must be one of "forehead", "eyes", '
                              '"mouth", or "chin".')

    def to_dict(self):
        return {'point': self.point,
                'x_shift': self.x_shift,
                'y_shift': self.y_shift,
                'scale': self.scale}
