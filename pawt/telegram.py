import requests

from .const import API_PATH, BASE_PATH
from .exceptions import APIException
from .models import Chat, File, Message, PhotoSize, Sticker, StickerSet, Update, \
    User


class Telegram:
    """The Telegram class provides access to the Telegram API."""

    def __init__(self, token, *, url=None, session=None, max_retries=3):
        """Create a Telegram instance.

        :param token: Telegram API token.
        :param url: The base url of the API you wish to use.
        Must contain `'{token}'`. (default:
        `'https://api.telegram.org/bot{token}/'`).

        """
        self.token = token

        self._url = url or BASE_PATH

        self.path = self._url.format(token=token)
        if not self.path.endswith('/'):
            self.path += '/'

        self.session = session or requests.Session()

        self._max_retries = max_retries

    def copy(self):
        """Return a copy of the Telegram object with a new session."""
        return Telegram(self.token, url=self._url)

    def chat(self, chat_id=None, data=None):
        return Chat(self, chat_id, data)

    def file(self, file_id=None, data=None):
        return File(self, file_id, data)

    def user(self, user_id=None, data=None):
        return User(self, user_id, data)

    def message(self, data):
        return Message(self, data)

    def photo_size(self, data):
        return PhotoSize(self, data)

    @staticmethod
    def _request_decoder(response):
        decoded = response.json()
        if not decoded['ok']:
            Telegram._raise_exception(decoded)
        return decoded['result']

    def _requestor(self, fn, *args, **kwargs):
        retries = 0
        while retries < self._max_retries:
            try:
                response = fn(*args, **kwargs)
            except requests.exceptions.ConnectionError as ce:
                retries += 1
                error = ce
            else:
                return response
        raise error

    def get(self, path, params=None):
        """Make a request.

        :param path: The path to add on to the base path.
        :param params: The parameters to send in the request. (default: None).

        """
        get = self.session.get
        response = self._requestor(get, self.path + path, params=params)
        return self._request_decoder(response)

    def post(self, path, data=None, files=None):
        post = self.session.post
        response = self._requestor(post, self.path + path, data=data,
                                   files=files)
        return self._request_decoder(response)

    def get_me(self):
        u = self.get(API_PATH['get_me'])
        return self.user(data=u)

    def get_updates(self, offset=None, limit=None, timeout=None,
                    allowed_updates=None):
        data = dict()
        if offset:
            data['offset'] = offset
        if limit:
            data['limit'] = limit
        if timeout:
            data['timeout'] = timeout
        if allowed_updates:
            data['allowed_updates'] = allowed_updates
        response = self.get(API_PATH['get_updates'], params=data)
        return [Update(self, ud) for ud in response]

    def sticker(self, data):
        return Sticker(self, data)

    def sticker_set(self, name):
        return StickerSet(self, name=name)

    @staticmethod
    def _raise_exception(data):
        if not data.get('parameters'):
            raise APIException(data['description'] + ' ({})'.format(
                data['error_code']))
        raise APIException('{} ({})\n\n{!r}'.format(data['description'],
                                                    data['error_code'],
                                                    data['parameters']))
