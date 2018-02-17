from .message import Message
from ..base import PAWTBase
from ..inline_queries import InlineQuery
from ..other_queries import CallbackQuery, ChosenInlineResult, \
    PreCheckoutQuery, ShippingQuery


class Update(PAWTBase):
    CONTENT_TYPES = ('message', 'edited_message', 'channel_post',
                     'edited_channel_post', 'inline_query',
                     'chosen_inline_result', 'callback_query',
                     'shipping_query', 'pre_checkout_query')
    TYPE_MAPPING = {'message': Message, 'edited_message': Message,
                    'channel_post': Message, 'edited_channel_post': Message,
                    'inline_query': InlineQuery,
                    'chosen_inline_result': ChosenInlineResult,
                    'callback_query': CallbackQuery,
                    'shipping_query': ShippingQuery,
                    'pre_checkout_query': PreCheckoutQuery}

    def __init__(self, tg, data):
        super().__init__(tg)
        self.id = data['update_id']
        self.content = None
        self.content_type = None

        self.message = self.edited_message = self.channel_post = None
        self.edited_channel_post = self.inline_query = None
        self.chosen_inline_result = self.callback_query = None
        self.shipping_query = self.pre_checkout_query = None

        # set the one and only piece of content to special vars for easier
        # accessibility.
        for content_type in Update.CONTENT_TYPES:
            if data.get(content_type):
                class_type = Update.TYPE_MAPPING[content_type]
                content_object = class_type(tg=tg, data=data[content_type])
                setattr(self, content_type, content_object)
                self.content = content_object
                self.content_type = content_type
                break  # there's only one

    def __repr__(self):
        return '<Update {}>'.format(self.id)

    def __str__(self):
        return '{} {}'.format(self.content_type, str(self.content))
