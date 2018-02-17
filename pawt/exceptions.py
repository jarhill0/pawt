class TelegramException(Exception):
    """Base class for all exceptions in PAWT."""


class APIException(TelegramException):
    """Class for all exceptions caused serverside."""


class BadArgument(TelegramException, ValueError):
    """Raised for values validated as bad prior to network requests."""


class CaptionOrTextTooLong(BadArgument):
    """Raised when a text field is too long. """


class BadType(TelegramException, TypeError):
    """Raised when trying to perform an operation on an object that doesn't
    support it."""
