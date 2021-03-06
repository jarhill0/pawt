from .base import FileWrapper
from ..base import Sendable


class VideoNote(FileWrapper, Sendable):
    def __init__(self, tg, data):
        super().__init__(tg, data)

        self.length = data["length"]
        self.duration = data["duration"]

        if data.get("thumb"):
            self.thumb = tg.photo_size(data=data["thumb"])
        else:
            self.thumb = None

    def send(self, chat, *args, **kwargs):
        chat = self._chat_parser(chat)
        return chat.send_video_note(self, *args, **kwargs)
