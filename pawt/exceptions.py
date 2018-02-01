class TelegramException(Exception):
    """Base class for all exceptions in PAWT."""
    pass


class APIException(TelegramException):
    """Class for all exceptions caused serverside."""


class BadArgument(TelegramException, ValueError):
    """Raised for values validated as bad prior to network requests."""
    pass


class BadType(TelegramException, TypeError):
    """Raised when trying to perform an operation on an object that doesn't
    support it."""
