from enum import Enum
from json import dumps

from .chat_member import ChatMember
from .chat_photo import ChatPhoto
from ..base import PAWTLazy
from ...const import API_PATH, MAX_LENGTH
from ...exceptions import BadArgument, TooLong
from ...models.message_specials import Photo, Video


class ChatType(Enum):
    private = 'private'
    group = 'group'
    supergroup = 'supergroup'
    channel = 'channel'


class Chat(PAWTLazy):
    CHAT_TYPES = [chat_type for chat_type in ChatType]
    CHAT_ACTIONS = ('typing', 'upload_photo', 'record_video', 'upload_video',
                    'record_audio', 'upload_audio', 'upload_document',
                    'find_location', 'record_video_note', 'upload_video_note')

    @staticmethod
    def _coerce_userlike_obj(user):
        if hasattr(user, 'id'):
            user = user.id
        return str(user)

    def __init__(self, tg, chat_id=None, data=None):
        super().__init__(tg)
        if bool(chat_id) == bool(data):
            raise BadArgument('Exactly one of chat_id and data must be given')

        self._fetched = bool(data)

        if chat_id:
            self.id = str(chat_id)
        if data:
            self._set_known_attrs(data)

    def __repr__(self):
        return '<Chat {}>'.format(self.id)

    def __str__(self):
        return self.title or str(self.id)

    def __eq__(self, other):
        if hasattr(other, 'id'):
            return str(self.id) == str(other.id)
        return str(self.id) == str(other)

    def _set_known_attrs(self, data):
        self.id = str(data['id'])
        self.type = ChatType(data['type'])
        self.title = data.get('title')
        self.username = data.get('username')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.all_members_are_administrators = data.get(
            'all_members_are_administrators')
        self.description = data.get('description')
        self.invite_link = data.get('invite_link')
        self.can_set_sticker_set = data.get('can_set_sticker_set')

        sticker_set_name = data.get('sticker_set_name')
        if sticker_set_name:
            self.sticker_set = self._tg.sticker_set(sticker_set_name)
        else:
            self.sticker_set = None

        photo = data.get('photo')
        if photo:
            self.photo = ChatPhoto(self._tg, photo)
        else:
            self.photo = None

        if data.get('pinned_message'):
            self.pinned_message = self._tg.message(data=data['pinned_message'])
        else:
            self.pinned_message = None

    def _load(self):
        data = self._tg.get(API_PATH['get_chat'], params=dict(chat_id=self.id))
        self._set_known_attrs(data)

    def get_chat(self):
        """Loads the chat in place."""
        self._load()

    def export_invite_link(self):
        return self._tg.get(API_PATH['export_chat_invite_link'],
                            params=dict(chat_id=self.id))

    def leave(self):
        return self._tg.post(API_PATH['leave_chat'], data=dict(chat_id=self.id))

    def get_member(self, user):
        user_id = self._coerce_userlike_obj(user)
        data = self._tg.get(API_PATH['get_chat_member'],
                            params=dict(chat_id=self.id, user_id=user_id))
        return ChatMember(self._tg, data)

    def get_administrators(self):
        data = self._tg.get(API_PATH['get_chat_administrators'],
                            params=dict(chat_id=self.id))
        return [ChatMember(self._tg, m) for m in data]

    def promote_member(self, user, **opts):
        user_id = self._coerce_userlike_obj(user)
        data = dict(chat_id=self.id, user_id=user_id)
        for option, value in opts.items():
            data[option] = value
        return self._tg.post(API_PATH['promote_chat_member'], data=data)

    def restrict_member(self, user, **opts):
        user_id = self._coerce_userlike_obj(user)
        data = dict(chat_id=self.id, user_id=user_id)
        for option, value in opts.items():
            data[option] = value
        return self._tg.post(API_PATH['restrict_chat_member'], data=data)

    def delete_photo(self):
        return self._tg.post(API_PATH['delete_chat_photo'],
                             data=dict(chat_id=self.id))

    def set_title(self, title):
        return self._tg.post(API_PATH['set_chat_title'],
                             data=dict(chat_id=self.id, title=title))

    def set_sticker_set(self, sticker_set):
        if hasattr(sticker_set, 'name'):
            sticker_set = sticker_set.name
        assert isinstance(sticker_set, str)
        return self._tg.post(API_PATH['set_chat_sticker_set'],
                             data=dict(chat_id=self.id,
                                       sticker_set_name=sticker_set))

    def delete_sticker_set(self):
        return self._tg.post(API_PATH['delete_chat_sticker_set'],
                             data=dict(chat_id=self.id))

    def set_description(self, description):
        return self._tg.post(API_PATH['set_chat_description'],
                             data=dict(chat_id=self.id,
                                       description=description))

    def set_photo(self, photo):
        return self._tg.post(API_PATH['set_chat_photo'],
                             data=dict(chat_id=self.id),
                             files=dict(photo=photo))

    def kick_member(self, user, until_date=None):
        user_id = self._coerce_userlike_obj(user)
        data = dict(user_id=user_id, chat_id=self.id)
        if until_date:
            data['until_date'] = until_date
        return self._tg.post(API_PATH['kick_chat_member'], data=data)

    def unban_member(self, user):
        user_id = self._coerce_userlike_obj(user)
        return self._tg.post(API_PATH['unban_chat_member'],
                             data=dict(chat_id=self.id,
                                       user_id=user_id))

    def pin_message(self, msg, disable_notification=None):
        if hasattr(msg, 'pin'):
            return msg.pin(disable_notification)

        data = dict(chat_id=self.id, message_id=str(msg))
        if disable_notification is not None:  # False is a possible val
            data['disable_notification'] = disable_notification
        return self._tg.post(API_PATH['pin_chat_message'], data=data)

    def get_member_count(self):
        return self._tg.get(API_PATH['get_chat_members_count'],
                            params=dict(chat_id=self.id))

    def unpin_message(self):
        return self._tg.post(API_PATH['unpin_chat_message'],
                             data=dict(chat_id=self.id))

    def _file_post_helper(self, api_path, data, possible_file,
                          file_param_name, files=None):
        caption = data.get('caption')
        if hasattr(possible_file, 'file'):
            possible_file = possible_file.file
        if hasattr(possible_file, 'id'):
            possible_file = possible_file.id
        if isinstance(possible_file, str):
            data[file_param_name] = possible_file
        else:
            if not files:
                files = dict()
            files[file_param_name] = possible_file

        if caption and len(caption) > MAX_LENGTH['caption']:
            msg = 'Caption is too long ({} > {})'.format(len(caption),
                                                         MAX_LENGTH['caption'])
            raise TooLong(self._tg, api_path, data, msg)

        response = self._tg.post(api_path, data=data, files=files)
        return self._tg.message(data=response)

    def _send_helper(self, disable_notification, reply_to, reply_markup):
        data = dict(chat_id=self.id)
        if disable_notification is not None:  # can be False
            data['disable_notification'] = disable_notification
        if reply_to:
            if hasattr(reply_to, 'id'):
                reply_to_message_id = reply_to.id
            else:
                reply_to_message_id = str(reply_to)
            data['reply_to_message_id'] = reply_to_message_id
        if reply_markup:
            data['reply_markup'] = dumps(reply_markup)
        return data

    def _post_and_return_message(self, api_path, data, files=None):
        text = data.get('text')
        if text and len(text) > MAX_LENGTH['text']:
            msg = 'Text is too long ({} > {})'.format(len(text),
                                                      MAX_LENGTH['text'])
            raise TooLong(self._tg, api_path, data, msg, files)

        response = self._tg.post(api_path, data=data, files=files)
        return self._tg.message(data=response)

    def send_message(self, text, parse_mode=None,
                     disable_web_page_preview=None,
                     disable_notification=None, reply_to=None,
                     reply_markup=None):

        data = self._send_helper(disable_notification, reply_to, reply_markup)
        data['text'] = text
        if parse_mode:
            data['parse_mode'] = parse_mode
        if disable_web_page_preview:
            data['disable_web_page_preview'] = disable_web_page_preview

        return self._post_and_return_message(API_PATH['send_message'], data)

    def send_document(self, document, caption=None, disable_notification=None,
                      reply_to=None, reply_markup=None):
        self.send_chat_action('upload_document')
        info = self._send_helper(disable_notification, reply_to, reply_markup)
        if caption:
            info['caption'] = caption
        return self._file_post_helper(API_PATH['send_document'], info,
                                      document, 'document')

    def send_video(self, video, duration=None, width=None, height=None,
                   caption=None, disable_notification=None, reply_to=None,
                   reply_markup=None):
        self.send_chat_action('upload_video')
        info = self._send_helper(disable_notification, reply_to, reply_markup)
        if duration:
            info['duration'] = duration
        if width:
            info['width'] = width
        if height:
            info['height'] = height
        if caption:
            info['caption'] = caption
        return self._file_post_helper(API_PATH['send_video'], info, video,
                                      'video')

    def send_voice(self, voice, caption=None, duration=None,
                   disable_notification=None, reply_to=None, reply_markup=None):
        self.send_chat_action('upload_audio')
        info = self._send_helper(disable_notification, reply_to, reply_markup)
        if caption:
            info['caption'] = caption
        if duration:
            info['duration'] = duration
        return self._file_post_helper(API_PATH['send_voice'], info, voice,
                                      'voice')

    def send_game(self, game_short_name, disable_notification=None,
                  reply_to=None, reply_markup=None):
        # can't make sendable because Game objects don't come with a shortname.
        info = self._send_helper(disable_notification, reply_to, reply_markup)
        info['game_short_name'] = game_short_name
        return self._post_and_return_message(API_PATH['send_game'], info)

    def send_photo(self, photo, caption=None, disable_notification=None,
                   reply_to=None, reply_markup=None):
        self.send_chat_action('upload_photo')
        info = self._send_helper(disable_notification, reply_to, reply_markup)
        if caption:
            info['caption'] = caption
        return self._file_post_helper(API_PATH['send_photo'], info, photo,
                                      'photo')

    def send_contact(self, contact=None, phone_number=None, first_name=None,
                     last_name=None, disable_notification=None, reply_to=None,
                     reply_markup=None):

        if contact and (phone_number or first_name or last_name):
            raise BadArgument('If contact is provided, phone_number, '
                              'first_name, and last_name should not be '
                              'provided.')
        if contact:
            phone_number = contact.phone_number
            first_name = contact.first_name
            last_name = contact.last_name

        info = self._send_helper(disable_notification, reply_to, reply_markup)
        info['phone_number'] = phone_number
        info['first_name'] = first_name
        if last_name:
            info['last_name'] = last_name
        return self._post_and_return_message(API_PATH['send_contact'], info)

    def send_media_group(self, media, disable_notification=None,
                         reply_to=None):

        if len(media) > 10 or len(media) < 2:
            raise BadArgument('media must have length between 2 and 10')

        info = self._send_helper(disable_notification, reply_to, None)

        builder = MediaGroupBuilder()
        for thing in media:
            if isinstance(thing, dict):
                builder.build_input_media(thing['type'], thing['media'],
                                          thing.get('caption'),
                                          thing.get('width'),
                                          thing.get('height'),
                                          thing.get('duration'))
            elif isinstance(thing, Photo):
                builder.build_input_media_photo(thing.max_size)
            elif isinstance(thing, Video):
                builder.build_input_media_video(thing, width=thing.width,
                                                height=thing.height,
                                                duration=thing.duration)
            else:
                raise BadArgument('Cannot handle thing of type {} as '
                                  'InputMedia.'.format(type(thing)))
        for item in builder.result:
            caption = item.get('caption')
            if caption and len(caption) > MAX_LENGTH['caption']:
                msg = 'Caption is too long ({} > {})'.format(len(caption),
                                                             MAX_LENGTH[
                                                                 'caption'])
                raise BadArgument(msg)

        info['media'] = dumps(builder.result)  # weird, I know.

        response = self._tg.post(API_PATH['send_media_group'], data=info,
                                 files=builder.files)
        return [self._tg.message(data=message) for message in response]

    def send_venue(self, venue=None, latitude=None, longitude=None, title=None,
                   address=None, foursquare_id=None, disable_notification=None,
                   reply_to=None, reply_markup=None):

        info = self._send_helper(disable_notification, reply_to, reply_markup)

        if venue and any((latitude, longitude, title, address, foursquare_id)):
            raise BadArgument('If venue is provided, latitude, longitude, '
                              'title, foursquare_id, and address should not be '
                              'provided.')

        if venue:
            latitude = venue.location.latitude
            longitude = venue.location.longitude
            title = venue.title
            address = venue.address
            foursquare_id = venue.foursquare_id

        info['latitude'] = latitude
        info['longitude'] = longitude
        info['title'] = title
        info['address'] = address
        if foursquare_id:
            info['foursquare_id'] = foursquare_id
        return self._post_and_return_message(API_PATH['send_venue'], info)

    def send_audio(self, audio, caption=None, duration=None, performer=None,
                   title=None, disable_notification=None, reply_to=None,
                   reply_markup=None):
        self.send_chat_action('upload_audio')
        info = self._send_helper(disable_notification, reply_to, reply_markup)
        if caption:
            info['caption'] = caption
        if duration:
            info['duration'] = duration
        if performer:
            info['performer'] = performer
        if title:
            info['title'] = title
        return self._file_post_helper(API_PATH['send_audio'], info, audio,
                                      'audio')

    def send_location(self, location=None, latitude=None, longitude=None,
                      live_period=None, disable_notification=None,
                      reply_to=None, reply_markup=None):

        if location and (latitude or longitude):
            raise BadArgument('If location is provided, latitude and '
                              'longitude should not be provided.')
        if location:
            latitude = location.latitude
            longitude = location.longitude

        info = self._send_helper(disable_notification, reply_to, reply_markup)
        info['latitude'] = latitude
        info['longitude'] = longitude
        if live_period:
            info['live_period'] = live_period

        return self._post_and_return_message(API_PATH['send_location'], info)

    def send_video_note(self, video_note, duration=None, length=None,
                        disable_notification=None, reply_to=None,
                        reply_markup=None):
        self.send_chat_action('upload_video_note')
        info = self._send_helper(disable_notification, reply_to, reply_markup)
        if duration:
            info['duration'] = duration
        if length:
            info['length'] = length
        return self._file_post_helper(API_PATH['send_video_note'], info,
                                      video_note, 'video_note')

    def send_chat_action(self, action):
        if action not in Chat.CHAT_ACTIONS:
            raise BadArgument('Action must be one of {!r}'.format(
                Chat.CHAT_ACTIONS))
        info = dict(chat_id=self.id, action=action)
        return self._tg.post(API_PATH['send_chat_action'], data=info)

    def send_invoice(self, title, description, payload, provider_token,
                     start_parameter, currency, prices, provider_data=None,
                     photo_url=None, photo_size=None, photo_width=None,
                     photo_height=None, need_name=None,
                     need_phone_number=None, need_email=None,
                     need_shipping_address=None,
                     send_phone_number_to_provider=None,
                     send_email_to_provider=None, is_flexible=None,
                     disable_notification=None, reply_to=None,
                     reply_markup=None):

        info = self._send_helper(disable_notification, reply_to, reply_markup)
        info['title'] = title
        info['description'] = description
        info['payload'] = payload
        info['provider_token'] = provider_token
        info['start_parameter'] = start_parameter
        info['currency'] = currency
        info['prices'] = dumps(prices)
        if provider_data:
            info['provider_data'] = provider_data
        if photo_url:
            info['photo_url'] = photo_url
        if photo_size:
            info['photo_size'] = photo_size
        if photo_width:
            info['photo_width'] = photo_width
        if photo_height:
            info['photo_height'] = photo_height
        if need_name is not None:  # can be False
            info['need_name'] = need_name
        if need_phone_number is not None:  # can be False
            info['need_phone_number'] = need_phone_number
        if need_email is not None:  # can be False
            info['need_email'] = need_email
        if need_shipping_address is not None:  # can be False
            info['need_shipping_address'] = need_shipping_address
        if send_phone_number_to_provider is not None:  # can be False
            shorter_name = send_phone_number_to_provider
            info['send_phone_number_to_provider'] = shorter_name
        if send_email_to_provider is not None:  # can be False
            info['send_email_to_provider'] = send_email_to_provider
        if is_flexible is not None:  # can be False
            info['is_flexible'] = is_flexible

        return self._post_and_return_message(API_PATH['send_invoice'], info)

    def forward_message(self, from_chat, message_id, disable_notification=None):
        info = self._send_helper(disable_notification, None, None)
        if hasattr(from_chat, 'id'):
            from_chat_id = from_chat.id
        else:
            from_chat_id = str(from_chat)
        info['from_chat_id'] = from_chat_id
        info['message_id'] = message_id
        return self._post_and_return_message(API_PATH['forward_message'], info)

    def send_sticker(self, sticker, disable_notification=None, reply_to=None,
                     reply_markup=None):
        info = self._send_helper(disable_notification, reply_to, reply_markup)
        if hasattr(sticker, 'file'):
            sticker = sticker.file.id
        return self._file_post_helper(API_PATH['send_sticker'], info, sticker,
                                      'sticker')


def make_labeled_price(label, amount):
    return dict(label=label, amount=amount)


class MediaGroupBuilder:
    def __init__(self):
        self.result = []
        self.files = {}
        self._file_number = 0

    def build_input_media(self, type_, media, caption=None, width=None,
                          height=None, duration=None):
        if isinstance(media, str):
            media_formatted = media  # assuming it's a URL
        elif hasattr(media, 'file'):
            media_formatted = media.file.id
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
