from ..base import PAWTLazy
from ...const import API_PATH
from ...exceptions import BadArgument


class File(PAWTLazy):
    DL_LINK = 'https://api.telegram.org/file/bot{token}/{file_path}'

    @property
    def link(self):
        """The link to download the file. Incompatible with alternate API
        URLs."""
        return File.DL_LINK.format(token=self._tg.token,
                                   file_path=self.file_path)

    def __init__(self, tg, file_id=None, data=None):
        super().__init__(tg)

        if bool(file_id) == bool(data):
            raise BadArgument('Exactly one of file_id and data should be '
                              'given.')

        if file_id:
            self.id = file_id
        if data:
            self._set_data(data)

    def __eq__(self, other):
        if hasattr(other, 'id'):
            return str(self.id) == str(other.id)
        return str(self.id) == str(other)

    def __repr__(self):
        return '<File {}>'.format(self.id)

    def _get_data(self):
        return self._tg.get(API_PATH['get_file'],
                            params=dict(file_id=self.id))

    def _set_data(self, data):
        self.id = data['file_id']
        self.file_size = data.get('file_size', None)
        self.file_path = data.get('file_path', None)

    def _load(self):
        self._set_data(self._get_data())

    def get_file(self):
        """Returns a new File instance with updated info."""
        return self._tg.file(data=self._get_data())

    def refresh(self):
        """Refreshes the attributes in place."""
        self._load()
