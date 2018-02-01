import sys

from ..telegram import Telegram

CONTENT_TYPES = ('message', 'edited_message', 'channel_post',
                 'edited_channel_post', 'inline_query',
                 'chosen_inline_result', 'callback_query',
                 'shipping_query', 'pre_checkout_query')


class TelegramBotInterface:
    """Base interface for all PAWT bots."""

    def __init__(self, token, *, url=None, session=None):
        self.tg = Telegram(token, url=url, session=session)
        self.update_offset = 0

    def run(self, timeout=60):
        while True:
            try:
                updates = self.tg.get_updates(self.update_offset, limit=100,
                                              timeout=timeout,
                                              allowed_updates=CONTENT_TYPES)

                if not updates:
                    self.perform_extra_task()
                    continue

                self.update_offset = max(u.id for u in updates) + 1
                for update in updates:
                    # what a nice little elif chain!
                    if update.content_type == 'message':
                        self.message_handler(update.message)
                    elif update.content_type == 'edited_message':
                        self.edited_message_handler(update.edited_message)
                    elif update.content_type == 'channel_post':
                        self.channel_post_handler(update.channel_post)
                    elif update.content_type == 'edited_channel_post':
                        self.edited_channel_post_handler(
                            update.edited_channel_post)
                    elif update.content_type == 'inline_query':
                        self.inline_query_handler(update.inline_query)
                    elif update.content_type == 'chosen_inline_result':
                        self.chosen_inline_result_handler(
                            update.chosen_inline_result)
                    elif update.content_type == 'callback_query':
                        self.callback_query_handler(update.callback_query)
                    elif update.content_type == 'shipping_query':
                        self.shipping_query_handler(update.shipping_query)
                    elif update.content_type == 'pre_checkout_query':
                        self.pre_checkout_query_handler(
                            update.pre_checkout_query)

                self.perform_extra_task()

            except KeyboardInterrupt:
                self.before_exit()
                sys.exit(0)

    def message_handler(self, message):
        pass

    def edited_message_handler(self, edited_message):
        pass

    def channel_post_handler(self, channel_post):
        pass

    def edited_channel_post_handler(self, edited_channel_post):
        pass

    def inline_query_handler(self, inline_query):
        pass

    def chosen_inline_result_handler(self, chosen_inline_result):
        pass

    def callback_query_handler(self, callback_query):
        pass

    def shipping_query_handler(self, shipping_query):
        pass

    def pre_checkout_query_handler(self, pre_checkout_query):
        pass

    def perform_extra_task(self):
        pass

    def before_exit(self):
        pass
