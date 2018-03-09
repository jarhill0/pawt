from .inline_query_result import InlineQueryResult


class InlineQueryResultVoice(InlineQueryResult):
    """Represents a link to a voice recording in an .ogg container encoded
    with OPUS. By default, this voice recording will be sent by the user.
    Alternatively, you can use input_message_content to send a message with
    the specified content instead of the the voice message."""

    def __init__(self, id_, voice_url, title, caption=None,
                 voice_duration=None, reply_markup=None,
                 input_message_content=None):
        super().__init__('voice', id_, reply_markup)

        self.voice_url = voice_url
        self.title = title
        self.caption = caption
        self.voice_duration = voice_duration
        self.input_message_content = None

        if input_message_content:
            self.input_message_content = input_message_content.to_dict()
