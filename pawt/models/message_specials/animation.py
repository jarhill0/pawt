from .base import FileWrapper
from ...models import photo_size


class Animation(FileWrapper):
    def __init__(self, tg, data):
        super().__init__(tg, data)

        self.file_name = data.get('file_name')
        self.mime_type = data.get('mime_type')

        if data.get('thumb'):
            self.thumb = photo_size.PhotoSize(tg, data['thumb'])
        else:
            self.thumb = None
