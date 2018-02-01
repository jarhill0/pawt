from .base import FileWrapper
from ..base import Sendable


class Voice(FileWrapper, Sendable):
    def __init__(self, tg, data):
        super().__init__(tg, data)

        self.duration = data['duration']
        self.mime_type = data.get('mime_type')

    def send(self, chat, *args, **kwargs):
        chat = self._chat_parser(chat)
        return chat.send_voice(self, *args, **kwargs)
