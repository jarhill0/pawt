from json import dumps

from ..base import PAWTBase
from .sticker import Sticker
from ..message_specials import Audio, Contact, Document, Game, GameHighScore, \
    Invoice, Location, MessageEntity, Photo, SuccessfulPayment as SucPy, \
    Venue, Video, VideoNote, Voice
from ...const import API_PATH
from ...exceptions import BadArgument, BadType


class Message(PAWTBase):
    def __init__(self, tg, data):
        super().__init__(tg)

        self.id = str(data['message_id'])
        self.date = data['date']
        self.chat = tg.chat(data=data['chat'])
        self.edit_date = data.get('edit_date')
        self.media_group_id = data.get('media_group_id')
        self.author_signature = data.get('author_signature')
        self.text = data.get('text')
        self.caption = data.get('caption')
        self.new_chat_title = data.get('new_chat_title')
        self.delete_chat_photo = data.get('delete_chat_photo')
        self.group_chat_created = data.get('group_chat_created')
        self.supergroup_chat_created = data.get('supergroup_chat_created')
        self.channel_chat_created = data.get('channel_chat_created')
        self.migrate_to_chat_id = data.get('migrate_to_chat_id')
        self.migrate_from_chat_id = data.get('migrate_from_chat_id')

        # redefined if they exist
        self.user = self.reply_to_message = self.photo = self.sticker = None
        self.new_chat_members = self.left_chat_member = None
        self.new_chat_photo = self.pinned_message = self.entities = None
        self.caption_entities = self.audio = self.document = self.game = None
        self.video = self.voice = self.video_note = self.contact = None
        self.location = self.venue = self.invoice = None
        self.successful_payment = None

        if data.get('from'):
            self.user = tg.user(data=data['from'])
        if data.get('reply_to_message'):
            self.reply_to_message = Message(tg, data=data['reply_to_message'])
        if data.get('photo'):
            self.photo = Photo(tg, data['photo'])
        if data.get('sticker'):
            self.sticker = Sticker(tg, data=data['sticker'])
        if data.get('new_chat_members'):
            self.new_chat_members = [tg.user(data=user_data)
                                     for user_data in data['new_chat_members']]
        if data.get('left_chat_member'):
            self.left_chat_member = tg.user(data=data['left_chat_member'])
        if data.get('new_chat_photo'):
            self.new_chat_photo = [tg.photo_size(data=ps)
                                   for ps in data['new_chat_photo']]
        if data.get('pinned_message'):
            self.pinned_message = Message(tg, data=data['pinned_message'])
        if data.get('entities'):
            self.entities = [MessageEntity.build(tg, me, self.text)
                             for me in data['entities']]
        if data.get('caption_entities'):
            self.caption_entities = [MessageEntity.build(tg, me, self.caption)
                                     for me in data['caption_entities']]
        if data.get('audio'):
            self.audio = Audio(tg, data=data['audio'])
        if data.get('document'):
            self.document = Document(tg, data=data['document'])
        if data.get('game'):
            self.game = Game(tg, data=data['game'])
        if data.get('video'):
            self.video = Video(tg, data=data['video'])
        if data.get('voice'):
            self.voice = Voice(tg, data=data['voice'])
        if data.get('video_note'):
            self.video_note = VideoNote(tg, data=data['video_note'])
        if data.get('contact'):
            self.contact = Contact(tg, data=data['contact'])
        if data.get('location'):
            self.location = Location(tg, data=data['location'])
        if data.get('venue'):
            self.venue = Venue(tg, data=data['venue'])
        if data.get('invoice'):
            self.invoice = Invoice(tg, data=data['invoice'])
        if data.get('successful_payment'):
            self.successful_payment = SucPy(tg, data=data['successful_payment'])

        if data.get('forward_from'):
            # assume it's a forward
            self.forward_from = tg.user(data=data['forward_from'])
            self.forward_date = data['forward_date']
        else:
            self.forward_from = self.forward_date = None
        if data.get('forward_from_chat'):
            # it's a forward from a channel
            self.forward_from_chat = tg.chat(data=data['forward_from_chat'])
            self.forward_from_message_id = data['forward_from_message_id']
            self.forward_signature = data['forward_signature']
        else:
            self.forward_from_chat = self.forward_from_message_id = None
            self.forward_signature = None

        self._replier = None

    @property
    def from_(self):
        # from is a reserved keyword, so this will have to do
        return self.user

    def get_text_content(self):
        return self.text or self.caption or ''

    def get_any_entities(self):
        return self.entities or self.caption_entities or []

    def __repr__(self):
        return '<Message {}>'.format(self.id)

    def pin(self, disable_notification=None):
        data = dict(chat_id=self.chat.id, message_id=self.id)
        if disable_notification is not None:
            data['disable_notification'] = disable_notification
        return self._tg.post(API_PATH['pin_chat_message'], data=data)

    def edit(self, new_text=None, parse_mode=None,
             disable_web_page_preview=None, reply_markup=None):

        data = dict(chat_id=self.chat.id, message_id=self.id)
        if reply_markup:
            data['reply_markup'] = dumps(reply_markup)  # yeah it's weird
        if self.text and new_text:
            # we're editing a text message
            data['text'] = new_text
            if parse_mode:
                data['parse_mode'] = parse_mode
            if disable_web_page_preview:
                data['disable_web_page_preview'] = disable_web_page_preview
            response = self._tg.post(API_PATH['edit_message_text'], data=data)
        else:
            if parse_mode or disable_web_page_preview:
                raise BadType("This Message doesn't support the parameters "
                              "parse_mode or disable_web_page_preview.")
            if new_text:
                # we're editing something with a caption
                data['caption'] = new_text
                response = self._tg.post(API_PATH['edit_message_caption'],
                                         data=data)
            else:
                # we're only editing the reply_markup
                if not reply_markup:
                    raise BadArgument("At least new_text or reply_markup must "
                                      "be provided.")
                response = self._tg.post(API_PATH['edit_message_reply_markup'],
                                         data=data)
        return Message(self._tg, response)

    def edit_live_location(self, latitude, longitude, reply_markup=None):

        info = dict(chat_id=self.chat.id, message_id=self.id, latitude=latitude,
                    longitude=longitude)
        if reply_markup:
            info['reply_markup'] = dumps(reply_markup)
        resp = self._tg.post(API_PATH['edit_message_live_location'], data=info)
        if resp == True:  # explicitly checking for True, not just truthy value
            return resp
        return Message(self._tg, data=resp)

    def stop_live_location(self, reply_markup=None):

        info = dict(chat_id=self.chat.id, message_id=self.id)
        if reply_markup:
            info['reply_markup'] = reply_markup
        resp = self._tg.post(API_PATH['stop_message_live_location'], data=info)
        if resp == True:  # explicitly checking for True, not just truthy value
            return resp
        return Message(self._tg, data=resp)

    def delete(self):
        return self._tg.post(API_PATH['delete_message'],
                             data=dict(chat_id=self.chat.id,
                                       message_id=self.id))

    @property
    def reply(self):
        if not self._replier:
            self._replier = MessageReplier(self._tg, self)
        return self._replier

    def forward(self, to_chat, *args, **kwargs):
        if isinstance(to_chat, (int, str)):
            to_chat = self._tg.chat(chat_id=to_chat)
        return to_chat.forward_message(self.chat.id, self.id, *args, **kwargs)

    def get_game_high_scores(self, user):
        if not isinstance(user, (str, int)):
            user_id = user.id
        else:
            user_id = str(user)
        data = dict(chat_id=self.chat.id, message_id=self.id, user_id=user_id)
        response = self._tg.post(API_PATH['get_game_high_scores'], data=data)
        return [GameHighScore(self._tg, data=ghs)
                for ghs in response]

    def set_game_score(self, user, score, force=False,
                       disable_edit_message=False):

        if not isinstance(user, (str, int)):
            user_id = user.id
        else:
            user_id = str(user)
        data = dict(chat_id=self.chat.id, message_id=self.id, score=score,
                    force=force, disable_edit_message=disable_edit_message,
                    user_id=user_id)
        response = self._tg.post(API_PATH['set_game_score'], data=data)
        if isinstance(response, bool):
            return response
        return Message(self._tg, data=response)


class MessageReplier(PAWTBase):
    """An ugly class to facilitate message replying. Maybe it should use
    *args and **kwargs…"""

    def __init__(self, tg, message):
        super().__init__(tg)
        # essentially copies the Chat that this message is from and overrides
        # the methods.
        self._message = message
        self.message_id = message.id
        self.chat = message.chat

    def __call__(self, *args, **kwargs):
        return self.send_message(*args, **kwargs)

    def send_sticker(self, sticker, disable_notification=None,
                     reply_markup=None):
        return self.chat.send_sticker(sticker, disable_notification,
                                      self.message_id,
                                      reply_markup)

    def send_invoice(self, title, description, payload, provider_token,
                     start_parameter, currency, prices, provider_data=None,
                     photo_url=None, photo_size=None, photo_width=None,
                     photo_height=None, need_name=None, need_phone_number=None,
                     need_email=None, need_shipping_address=None,
                     send_phone_number_to_provider=None,
                     send_email_to_provider=None, is_flexible=None,
                     disable_notification=None,
                     reply_markup=None):
        return self.chat.send_invoice(title, description, payload,
                                      provider_token,
                                      start_parameter, currency, prices,
                                      provider_data, photo_url, photo_size,
                                      photo_width, photo_height, need_name,
                                      need_phone_number, need_email,
                                      need_shipping_address,
                                      send_phone_number_to_provider,
                                      send_email_to_provider, is_flexible,
                                      disable_notification, self.message_id,
                                      reply_markup)

    def send_location(self, location=None, latitude=None, longitude=None,
                      live_period=None, disable_notification=None,
                      reply_markup=None):
        return self.chat.send_location(location, latitude, longitude,
                                       live_period,
                                       disable_notification, self.message_id,
                                       reply_markup)

    def send_photo(self, photo, caption=None, disable_notification=None,
                   reply_markup=None):
        return self.chat.send_photo(photo, caption, disable_notification,
                                    self.message_id, reply_markup)

    def send_media_group(self, media, disable_notification=None, ):
        return self.chat.send_media_group(media, disable_notification,
                                          self.message_id)

    def send_game(self, game_short_name, disable_notification=None,
                  reply_markup=None):
        return self.chat.send_game(game_short_name, disable_notification,
                                   self.message_id, reply_markup)

    def __repr__(self):
        return '<MessageReplier for {!r}>'.format(self._message)

    def send_audio(self, audio, caption=None, duration=None, performer=None,
                   title=None, disable_notification=None,
                   reply_markup=None):
        return self.chat.send_audio(audio, caption, duration, performer, title,
                                    disable_notification, self.message_id,
                                    reply_markup)

    def send_video(self, video, duration=None, width=None, height=None,
                   caption=None, disable_notification=None,
                   reply_markup=None):
        return self.chat.send_video(video, duration, width, height, caption,
                                    disable_notification, self.message_id,
                                    reply_markup)

    def send_venue(self, venue=None, latitude=None, longitude=None, title=None,
                   address=None, foursquare_id=None, disable_notification=None,
                   reply_markup=None):
        return self.chat.send_venue(venue, latitude, longitude, title, address,
                                    foursquare_id, disable_notification,
                                    self.message_id,
                                    reply_markup)

    def send_voice(self, voice, caption=None, duration=None,
                   disable_notification=None, reply_markup=None):
        return self.chat.send_voice(voice, caption, duration,
                                    disable_notification, self.message_id,
                                    reply_markup)

    def send_contact(self, contact=None, phone_number=None, first_name=None,
                     last_name=None, disable_notification=None,
                     reply_markup=None):
        return self.chat.send_contact(contact, phone_number, first_name,
                                      last_name, disable_notification,
                                      self.message_id,
                                      reply_markup)

    def send_document(self, document, caption=None, disable_notification=None,
                      reply_markup=None):
        return self.chat.send_document(document, caption, disable_notification,
                                       self.message_id, reply_markup)

    def send_video_note(self, video_note, duration=None, length=None,
                        disable_notification=None,
                        reply_markup=None):
        return self.chat.send_video_note(video_note, duration, length,
                                         disable_notification, self.message_id,
                                         reply_markup)

    def send_message(self, text, parse_mode=None, disable_web_page_preview=None,
                     disable_notification=None,
                     reply_markup=None):
        return self.chat.send_message(text, parse_mode,
                                      disable_web_page_preview,
                                      disable_notification, self.message_id,
                                      reply_markup)
