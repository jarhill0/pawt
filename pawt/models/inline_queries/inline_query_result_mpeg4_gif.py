from .inline_query_result import InlineQueryResult


class InlineQueryResultMpeg4Gif(InlineQueryResult):
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without
    sound). By default, this animated MPEG-4 file will be sent by the user with
    optional caption. Alternatively, you can use input_message_content to send a
    message with the specified content instead of the animation."""

    def __init__(self, id_, mpeg4_url, thumb_url, mpeg4_width=None,
                 mpeg4_height=None, mpeg4_duration=None, title=None,
                 caption=None, reply_markup=None, input_message_content=None):
        super().__init__('mpeg4_gif', id_, reply_markup)

        self.mpeg4_url = mpeg4_url
        self.thumb_url = thumb_url
        self.mpeg4_width = mpeg4_width
        self.mpeg4_height = mpeg4_height
        self.mpeg4_duration = mpeg4_duration
        self.title = title
        self.caption = caption
        self.input_message_content = input_message_content.to_dict()
