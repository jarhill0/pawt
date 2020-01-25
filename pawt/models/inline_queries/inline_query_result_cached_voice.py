from .inline_query_result import InlineQueryResult


class InlineQueryResultCachedVoice(InlineQueryResult):
    """Represents a link to a voice message stored on the Telegram servers. By
    default, this voice message will be sent by the user. Alternatively, you
    can use input_message_content to send a message with the specified content
    instead of the voice message."""

    def __init__(
        self,
        id_,
        voice_file_id,
        title,
        caption=None,
        reply_markup=None,
        input_message_content=None,
    ):
        super().__init__("voice", id_, reply_markup)

        self.voice_file_id = voice_file_id
        self.title = title
        self.caption = caption
        self.input_message_content = None

        if input_message_content:
            self.input_message_content = input_message_content.to_dict()
