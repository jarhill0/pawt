from json import dumps

from .user_profile_photos import UserProfilePhotos
from ..base import PAWTBase
from ...const import API_PATH
from ...exceptions import BadArgument


class User(PAWTBase):
    @property
    def full_name(self):
        if not self.first_name:
            return ''
        if self.last_name:
            return '{} {}'.format(self.first_name, self.last_name)
        return self.first_name

    def __init__(self, tg, user_id=None, data=None):
        super(User, self).__init__(tg)

        if bool(user_id) == bool(data):
            raise BadArgument('Exactly one of user_id and data must be given')

        if user_id:
            self.id = str(user_id)
            self.is_bot = None
            self.first_name = None
            self.last_name = None
            self.username = None
            self.language_code = None

        if data:
            self.id = str(data['id'])
            self.is_bot = data['is_bot']
            self.first_name = data['first_name']
            self.last_name = data.get('last_name')
            self.username = data.get('username')
            self.language_code = data.get('language_code')

    def __repr__(self):
        return '<User {id}>'.format(id=self.id)

    def __str__(self):
        return self.full_name

    def __eq__(self, other):
        return ((hasattr(other, 'id') and str(self.id) == str(other.id)) or
                str(self.id) == str(other))

    @property
    def chat(self):
        """Get a chat object out of the user"""
        return self._tg.chat(self.id)

    def add_sticker_to_set(self, name, png_sticker, emojis, mask_position=None):
        if not isinstance(png_sticker, str):
            png_sticker = self.upload_sticker_file(png_sticker).id
        return self._tg.post(API_PATH['add_sticker_to_set'],
                             data=dict(user_id=self.id,
                                       name=name,
                                       png_sticker=png_sticker,
                                       emojis=emojis,
                                       mask_position=mask_position))

    def create_new_sticker_set(self, name, title, png_sticker, emojis,
                               mask_position=None):

        data = dict(user_id=self.id,
                    name=name,
                    title=title,
                    emojis=emojis)
        contains_masks = bool(mask_position)
        if contains_masks:
            data['contains_masks'] = True
            data['mask_position'] = dumps(mask_position.to_dict())

        if not (isinstance(png_sticker, str) or hasattr(png_sticker, 'id')):
            png_sticker = self.upload_sticker_file(png_sticker)
        if hasattr(png_sticker, 'id'):
            png_sticker = png_sticker.id
        data['png_sticker'] = png_sticker
        return self._tg.get(API_PATH['create_new_sticker_set'], params=data)

    def get_profile_photos(self, offset=None, limit=None):
        if (limit is not None) and (limit < 1 or limit > 100):
            raise BadArgument('limit must be between 1 and 100.')
        data = dict(user_id=self.id)
        if offset:
            data['offset'] = offset
        if limit:
            data['limit'] = limit
        response = self._tg.get(API_PATH['get_user_profile_photos'],
                                params=data)
        return UserProfilePhotos(self._tg, response)

    def upload_sticker_file(self, png_sticker):
        data = self._tg.post(API_PATH['upload_sticker_file'],
                             files=dict(png_sticker=png_sticker),
                             data=dict(user_id=self.id))
        return self._tg.file(data=data)
