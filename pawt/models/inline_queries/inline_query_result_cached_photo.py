from .inline_query_result import InlineQueryResult


class InlineQueryResultCachedPhoto(InlineQueryResult):
    """Represents a link to a photo stored on the Telegram servers. By default,
    this photo will be sent by the user with an optional caption. Alternatively,
    you can use input_message_content to send a message with the specified
    content instead of the photo."""

    def __init__(
        self,
        id_,
        photo_file_id,
        title=None,
        description=None,
        caption=None,
        reply_markup=None,
        input_message_content=None,
    ):
        super().__init__("photo", id_, reply_markup)

        self.photo_file_id = photo_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.input_message_content = None

        if input_message_content:
            self.input_message_content = input_message_content.to_dict()
