from .inline_query_result import InlineQueryResult


class InlineQueryResultCachedGif(InlineQueryResult):
    """Represents a link to an animated GIF file stored on the Telegram
    servers. By default, this animated GIF file will be sent by the user with
    an optional caption. Alternatively, you can use input_message_content to
    send a message with specified content instead of the animation."""

    def __init__(self, id_, gif_file_id, title=None, caption=None,
                 reply_markup=None, input_message_content=None):
        super().__init__('gif', id_, reply_markup)

        self.gif_file_id = gif_file_id
        self.title = title
        self.caption = caption
        self.input_message_content = None

        if input_message_content:
            self.input_message_content = input_message_content.to_dict()
