from .base import FileWrapper
from ..base import Sendable


class Video(FileWrapper, Sendable):
    def __init__(self, tg, data):
        super().__init__(tg, data)

        self.width = data["width"]
        self.height = data["height"]
        self.duration = data["duration"]
        self.mime_type = data.get("mime_type")

        if data.get("thumb"):
            self.thumb = tg.photo_size(data=data["thumb"])
        else:
            self.thumb = None

    def send(self, chat, *args, **kwargs):
        chat = self._chat_parser(chat)
        return chat.send_video(self, *args, **kwargs)
