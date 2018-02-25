from copy import deepcopy

from .const import MAX_LENGTH


class TelegramException(Exception):
    """Base class for all exceptions in PAWT."""


class APIException(TelegramException):
    """Class for all exceptions caused serverside."""

    def __init__(self, data):
        message = '{}: {}'.format(data['error_code'], data['description'])
        self.response_parameters = data.get('parameters')
        super().__init__(message)


class BadArgument(TelegramException, ValueError):
    """Raised for values validated as bad prior to network requests."""


class TooLong(BadArgument):
    """Raised when a text field is too long. """

    def __init__(self, tg, api_path, data, *args, files=None) -> None:
        super().__init__(*args)
        self._path = api_path
        self._data = deepcopy(data)
        self._tg = tg
        self._files = files

    def send_chunked(self):
        """Method to automatically re-send a message in chunks."""
        param_name = 'text' if self._data.get('text') else 'caption'
        # this method won't work on a long amount of text separated by
        # non-space whitespace.
        original = self._data[param_name].split(' ')
        if any(len(part) > MAX_LENGTH[param_name] for part in original):
            # we can't do it gracefully
            self._dummy_mode()
            return

        # helper -- better than copy-paste!
        def send():
            message = ' '.join(this_chunk)
            self._data[param_name] = message
            self._tg.post(self._path, data=self._data, files=self._files)

        this_chunk = []
        total_len = -1  # -1 to account for one extra space
        for part in original:
            part_len = len(part)
            if total_len + part_len > MAX_LENGTH[param_name]:
                send()
                this_chunk = []
                total_len = -1
            this_chunk.append(part)
            total_len += 1 + part_len  # the 1 for the space
        send()

    def _dummy_mode(self):
        """Mangle the text in perfect chunks."""
        param_name = 'text' if self._data.get('text') else 'caption'
        text = self._data[param_name]
        size = MAX_LENGTH[param_name]
        for i in range(0, len(text), size):
            chunk = text[i:i + size]
            self._data[param_name] = chunk
            self._tg.post(self._path, data=self._data, files=self._files)


class BadType(TelegramException, TypeError):
    """Raised when trying to perform an operation on an object that doesn't
    support it."""
