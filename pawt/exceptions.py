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


class CaptionOrTextTooLong(BadArgument):
    """Raised when a text field is too long. """


class BadType(TelegramException, TypeError):
    """Raised when trying to perform an operation on an object that doesn't
    support it."""
