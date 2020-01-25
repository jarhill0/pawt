from .inline_query_result import InlineQueryResult


class InlineQueryResultCachedDocument(InlineQueryResult):
    """Represents a link to a file stored on the Telegram servers. By default,
    this file will be sent by the user with an optional caption.
    Alternatively, you can use input_message_content to send a message with the
    specified content instead of the file."""

    def __init__(
        self,
        id_,
        title,
        document_file_id,
        description=None,
        caption=None,
        reply_markup=None,
        input_message_content=None,
    ):
        super().__init__("document", id_, reply_markup)

        self.title = title
        self.document_file_id = document_file_id
        self.description = description
        self.caption = caption
        self.input_message_content = None

        if input_message_content:
            self.input_message_content = input_message_content.to_dict()
