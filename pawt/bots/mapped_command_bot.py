from .command_bot import CommandBot


class MappedCommandBot(CommandBot):
    def __init__(self, token, text_command_map, caption_command_map, *,
                 url=None, session=None):
        super().__init__(token, url=url, session=session)
        self.text_command_map = text_command_map or dict()
        self.caption_command_map = caption_command_map or dict()
        assert all(command.islower() for command in self.text_command_map)
        assert all(command.islower() for command in self.caption_command_map)

    def text_command_handler(self, message, command_lowered, command_params):
        handler = self.text_command_map.get(command_lowered)
        if handler:
            handler(message, command_params)

    def caption_command_handler(self, message, command_lowered, command_params):
        handler = self.caption_command_map.get(command_lowered)
        if handler:
            handler(message, command_params)
