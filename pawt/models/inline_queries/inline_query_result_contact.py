from .inline_query_result import InlineQueryResult


class InlineQueryResultContact(InlineQueryResult):
    """Represents a contact with a phone number. By default, this contact will
    be sent by the user. Alternatively, you can use input_message_content to
    send a message with the specified content instead of the contact."""

    def __init__(self, id_, phone_number, first_name, last_name=None,
                 reply_markup=None, input_message_content=None, thumb_url=None,
                 thumb_width=None, thumb_height=None):
        super().__init__('contact', id_, reply_markup)

        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        self.input_message_content = None

        if input_message_content:
            self.input_message_content = input_message_content.to_dict()
