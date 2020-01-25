from ..base import PAWTBase


class ChatPhoto(PAWTBase):
    @property
    def big_file(self):
        return self._tg.file(file_id=self._big_file_id)

    @property
    def small_file(self):
        return self._tg.file(file_id=self._small_file_id)

    def __init__(self, tg, data):
        super().__init__(tg)

        self._small_file_id = data["small_file_id"]
        self._big_file_id = data["big_file_id"]
