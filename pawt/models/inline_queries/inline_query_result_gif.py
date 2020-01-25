from .inline_query_result import InlineQueryResult


class InlineQueryResultGif(InlineQueryResult):
    """Represents a link to an animated GIF file. By default, this animated
    GIF file will be sent by the user with optional caption. Alternatively,
    you can use input_message_content to send a message with the specified
    content instead of the animation."""

    def __init__(
        self,
        id_,
        gif_url,
        thumb_url,
        gif_width=None,
        gif_height=None,
        gif_duration=None,
        title=None,
        caption=None,
        reply_markup=None,
        input_message_content=None,
    ):
        super().__init__("gif", id_, reply_markup)

        self.gif_url = gif_url
        self.thumb_url = thumb_url
        self.gif_width = gif_width
        self.gif_height = gif_height
        self.gif_duration = gif_duration
        self.title = title
        self.caption = caption
        self.input_message_content = None

        if input_message_content:
            self.input_message_content = input_message_content.to_dict()
