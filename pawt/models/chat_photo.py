from .base import PAWTBase


class ChatPhoto(PAWTBase):
    def __init__(self, tg, data):
        super().__init__(tg)

        self.small_file_id = data['small_file_id']
        self.big_file_id = data['big_file_id']

    def get_small_file(self):
        return self._tg.file(file_id=self.small_file_id)

    def get_big_file(self):
        return self._tg.file(file_id=self.big_file_id)
