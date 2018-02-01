from .input_message_content import InputMessageContent


class InputContactMessageContent(InputMessageContent):
    def __init__(self, phone_number, first_name, last_name=None):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
