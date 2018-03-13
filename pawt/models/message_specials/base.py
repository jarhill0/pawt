from ..base import PAWTBase


class FileWrapper(PAWTBase):
    def __init__(self, tg, data):
        super().__init__(tg)

        self.file = self._tg.file(file_id=data['file_id'])
        self.file_size = data.get('file_size')

    def __repr__(self):
        return '<{class_name} {file_id}>'.format(
            class_name=self.__class__.__name__,
            file_id=self.file.id
        )

    def __eq__(self, other):
        if hasattr(other, 'file'):
            return self.file == other.file
        return str(other) == str(self.file.id)
