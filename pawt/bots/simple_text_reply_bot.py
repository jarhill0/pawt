from pawt.models.message_specials import BotCommand
from .bot import TelegramBotInterface


class SimpleTextReplyBot(TelegramBotInterface):
    def __init__(self, token, mapping, ignore_case=True, *, url=None,
                 session=None):
        super().__init__(token, url=url, session=session)

        self.ignore_case = ignore_case
        if ignore_case:
            keys = list(mapping.keys())
            for key in keys:
                mapping[key.lower()] = mapping[key]
        self.mapping = mapping

    def all_message_hander(self, message):
        entities = message.get_any_entities()
        for ent in entities:
            if not isinstance(ent, BotCommand):
                continue
            response = self.get_response(ent.command)
            if response:
                message.reply.send_message(response)

    def get_response(self, command):
        if self.ignore_case:
            command = command.lower()
        return self.mapping.get(command)

    def edited_channel_post_handler(self, edited_channel_post):
        self.all_message_hander(edited_channel_post)

    def edited_message_handler(self, edited_message):
        self.all_message_hander(edited_message)

    def channel_post_handler(self, channel_post):
        self.all_message_hander(channel_post)

    def message_handler(self, message):
        self.all_message_hander(message)
