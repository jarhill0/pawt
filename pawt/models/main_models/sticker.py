from ..base import PAWTBase, Sendable
from ..message_specials import FileWrapper
from ...const import API_PATH
from ...exceptions import BadArgument


class Sticker(FileWrapper, Sendable):
    # rewrote this class and I'm positive it broke things. Meh.
    def __init__(self, tg, data):
        super().__init__(tg, data)

        self.width = data["width"]
        self.height = data["height"]
        self.emoji = data.get("emoji")
        self.set_name = data.get("set_name")

        if data.get("thumb"):
            self.thumb = tg.photo_size(data=data["thumb"])
        else:
            self.thumb = None
        if data.get("mask_position"):
            self.mask_position = MaskPosition(data["mask_position"])
        else:
            self.mask_position = None

    def __eq__(self, other):
        return hasattr(other, "file") and self.file == other.file

    def delete(self):
        return self._tg.get(
            API_PATH["delete_sticker_from_set"], params={"sticker": self.file.id}
        )

    def get_set(self):
        return self._tg.sticker_set(self.set_name)

    def set_position(self, position):
        return self._tg.post(
            API_PATH["set_sticker_position_in_set"],
            data={"sticker": self.file.id, "position": position},
        )

    def send(self, chat, *args, **kwargs):
        chat = self._chat_parser(chat)
        return chat.send_sticker(self, *args, **kwargs)


class MaskPosition(PAWTBase):
    def __init__(self, data=None, point=None, x_shift=0, y_shift=0, scale=1):
        super().__init__(tg=None)

        if bool(data) == any((point, x_shift, y_shift, scale != 1)):
            raise BadArgument("Either data or the other attributes must be " "provided")

        if data:
            point = data["point"]
            x_shift = data["x_shift"]
            y_shift = data["y_shift"]
            scale = data["scale"]

        self.point = point
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.scale = scale

        if self.point not in ("forehead", "eyes", "mouth", "chin"):
            raise BadArgument(
                'Point must be one of "forehead", "eyes", ' '"mouth", or "chin".'
            )

    def to_dict(self):
        return {
            "point": self.point,
            "x_shift": self.x_shift,
            "y_shift": self.y_shift,
            "scale": self.scale,
        }
