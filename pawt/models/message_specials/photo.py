from ..base import Sendable


class Photo(Sendable):
    def __init__(self, tg, sizes):
        super().__init__(tg)

        self.sizes = [tg.photo_size(data=ps) for ps in sizes]

    @property
    def min_size(self):
        return min(self.sizes)

    @property
    def max_size(self):
        return max(self.sizes)

    def __repr__(self) -> str:
        return '<Photo ({} sizes)>'.format(len(self.sizes))

    def __getitem__(self, ind):
        return self.sizes[ind]

    def send(self, chat, *args, **kwargs):
        chat = self._chat_parser(chat)
        return chat.send_photo(self.max_size, *args, **kwargs)
