from ..base import Sendable
from ...models import photo_size


class Photo(Sendable):
    def __init__(self, tg, sizes):
        super().__init__(tg)

        self.sizes = [photo_size.PhotoSize(tg, data=ps) for ps in sizes]

    @property
    def min_size(self):
        return min(self.sizes)

    @property
    def max_size(self):
        return max(self.sizes)

    def __repr__(self) -> str:
        return '<Photo with {} sizes>'.format(len(self.sizes))

    def send(self, chat, *args, **kwargs):
        chat = self._chat_parser(chat)
        return chat.send_photo(self.max_size, *args, **kwargs)
