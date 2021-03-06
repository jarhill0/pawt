from .base import FileWrapper
from ..base import Sendable


class Document(FileWrapper, Sendable):
    def __init__(self, tg, data):
        super().__init__(tg, data)

        self.file_name = data.get("file_name")
        self.mime_type = data.get("mime_type")

        if data.get("thumb"):
            self.thumb = tg.photo_size(data=data["thumb"])
        else:
            self.thumb = None

    def send(self, chat, *args, **kwargs):
        chat = self._chat_parser(chat)
        return chat.send_document(self, *args, **kwargs)
