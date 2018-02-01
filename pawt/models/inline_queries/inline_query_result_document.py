from .inline_query_result import InlineQueryResult


class InlineQueryResultDocument(InlineQueryResult):
    """Represents a link to a file. By default, this file will be sent by the
    user with an optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the file. Currently, only .PDF and .ZIP files can be sent
    using this method."""

    def __init__(self, id_, title, document_url, mime_type, caption=None,
                 description=None, reply_markup=None,
                 input_message_content=None, thumb_url=None, thumb_width=None,
                 thumb_height=None):
        super().__init__('document', id_, reply_markup)

        self.title = title
        self.document_url = document_url
        self.mime_type = mime_type
        self.caption = caption
        self.description = description
        self.input_message_content = input_message_content.to_dict()
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
