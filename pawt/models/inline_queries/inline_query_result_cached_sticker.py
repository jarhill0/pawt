from .inline_query_result import InlineQueryResult


class InlineQueryResultCachedSticker(InlineQueryResult):
    """Represents a link to a sticker stored on the Telegram servers.
    By default, this sticker will be sent by the user. Alternatively, you can
    use input_message_content to send a message with the specified content
    instead of the sticker."""

    def __init__(
        self, id_, sticker_file_id, reply_markup=None, input_message_content=None
    ):
        super().__init__("sticker", id_, reply_markup)

        self.sticker_file_id = sticker_file_id
        self.input_message_content = None

        if input_message_content:
            self.input_message_content = input_message_content.to_dict()
