from .base import PAWTBase
from .message_specials import FileWrapper
from ..const import API_PATH
from ..exceptions import BadArgument
from ..models import file, user_profile_photos


class User(PAWTBase):
    @property
    def full_name(self):
        if not self.first_name:
            return ''
        if self.last_name:
            return '{} {}'.format(self.first_name, self.last_name)
        return self.first_name

    def __init__(self, tg, data=None, user_id=None):
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
        return hasattr(other, 'id') and str(self.id) == str(other.id)

    def add_sticker_to_set(self, name, png_sticker, emojis, mask_position=None):
        if not isinstance(png_sticker, (str, file.File, FileWrapper)):
            png_sticker = self.upload_sticker_file(png_sticker)
        if isinstance(png_sticker, file.File):
            png_sticker = png_sticker.id
        if isinstance(png_sticker, FileWrapper):
            png_sticker = png_sticker.file.id

        return self._tg.get(API_PATH['add_sticker_to_set'],
                            data=dict(user_id=self.id,
                                      name=name,
                                      png_sticker=png_sticker,
                                      emojis=emojis,
                                      mask_position=mask_position))

    def create_new_sticker_set(self, name, title, png_sticker, emojis,
                               contains_masks=None, mask_position=None):
        # validate name to save a network request if it is bad
        if not all(l.isalnum() or l == '_' for l in name):
            raise BadArgument('Name can contain only english letters, digits '
                              'and underscores')
        if not name[0].isalpha():
            raise BadArgument('Name must begin with a letter')
        if '__' in name:
            raise BadArgument("Name can't contain consecutive underscores")
        if len(name) < 1 or len(name) > 64:
            raise BadArgument('Name must be 1-64 characters')
        if not name.endswith('_by_{}'.format(self._tg.get_me().username)):
            raise BadArgument('Name must end in "_by_<bot username>"')

        # validate title
        if len(title) < 1 or len(title) > 64:
            raise BadArgument('Title must be 1-64 characters')

        data = dict(user_id=self.id,
                    name=name,
                    title=title,
                    emojis=emojis)
        if contains_masks:
            data['contains_masks'] = True
            if mask_position is None:
                raise BadArgument('If contains_masks is truthy, mask_position '
                                  'must be provided.')
            data['mask_position'] = mask_position.to_dict()

        if not isinstance(png_sticker, (str, file.File)):
            png_sticker = self.upload_sticker_file(png_sticker)
        if isinstance(png_sticker, file.File):
            png_sticker = png_sticker.id
        data['png_sticker'] = png_sticker
        return self._tg.get(API_PATH['create_new_sticker_set'], data=data)

    def get_profile_photos(self, offset=None, limit=None):
        if (limit is not None) and (limit < 1 or limit > 100):
            raise BadArgument('limit must be between 1 and 100.')
        data = dict(user_id=self.id)
        if offset:
            data['offset'] = offset
        if limit:
            data['limit'] = limit
        response = self._tg.get(API_PATH['get_user_profile_photos'],
                                data=data)
        return user_profile_photos.UserProfilePhotos(self._tg, response)

    def upload_sticker_file(self, png_sticker):
        data = self._tg.get(API_PATH['upload_sticker_file'],
                            files=dict(png_sticker=png_sticker),
                            data=dict(user_id=self.id))
        return self._tg.file(data=data)
