from .bot import TelegramBotInterface
from ..models.message_specials import BotCommand


class CommandBot(TelegramBotInterface):
    def text_command_handler(self, message, command_lowered, command_params):
        pass

    def caption_command_handler(self, message, command_lowered, command_params):
        pass

    def message_handler(self, message):
        self._handle_message(message)

    def edited_message_handler(self, edited_message):
        self._handle_message(edited_message)

    def channel_post_handler(self, channel_post):
        self._handle_message(channel_post)

    def edited_channel_post_handler(self, edited_channel_post):
        self._handle_message(edited_channel_post)

    @staticmethod
    def next_cmd_ind(entities, entity):
        for potential_e in entities[entities.index(entity) + 1 :]:
            if isinstance(potential_e, BotCommand):
                return potential_e.offset  # next command found
        return None  # no other command

    def _handle_message(self, message):
        if message.entities:  # text message — entities are text-based.
            for entity in message.entities:
                if isinstance(entity, BotCommand):
                    command = entity.command.lower()
                    end = self.next_cmd_ind(message.entities, entity)
                    cmd_text = message.text[entity.offset : end]
                    self.text_command_handler(message, command, cmd_text)
        elif message.caption_entities:  # entities are caption-related
            for entity in message.caption_entities:
                if isinstance(entity, BotCommand):
                    command = entity.command.lower()
                    end = self.next_cmd_ind(message.caption_entities, entity)
                    cmd_text = message.caption[entity.offset : end]
                    self.caption_command_handler(message, command, cmd_text)
