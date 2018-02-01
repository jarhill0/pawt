from .file import File
from .message_specials.base import FileWrapper


class MediaGroupBuilder:
    def __init__(self):
        self.result = []
        self.files = {}
        self._file_number = 0

    def build_input_media(self, type_, media, caption=None, width=None,
                          height=None, duration=None):
        if isinstance(media, str):
            media_formatted = media  # assuming it's a URL
        elif isinstance(media, FileWrapper):
            media_formatted = media.file.id
        elif isinstance(media, File):
            media_formatted = media.id  # it's a known File
        else:
            # assuming it's a file on disk
            name = 'file{}'.format(self._file_number)
            media_formatted = 'attach://{}'.format(name)
            self.files[name] = media
            self._file_number += 1

        data = dict(type=type_, media=media_formatted)
        if caption:
            data['caption'] = caption
        if width:
            data['width'] = width
        if height:
            data['height'] = height
        if duration:
            data['duration'] = duration

        self.result.append(data)

    def build_input_media_photo(self, media, caption=None):
        self.build_input_media('photo', media, caption)

    def build_input_media_video(self, media, caption=None, width=None,
                                height=None,
                                duration=None):
        self.build_input_media('video', media, caption, width, height, duration)
