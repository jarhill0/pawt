from .inline_query_result import InlineQueryResult


class InlineQueryResultCachedMpeg4Gif(InlineQueryResult):
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without
    sound) stored on the Telegram servers. By default, this animated MPEG-4
    file will be sent by the user with an optional caption. Alternatively, you
    can use input_message_content to send a message with the specified content
    instead of the animation."""

    def __init__(self, id_, mpeg4_file_id, title=None, caption=None,
                 reply_markup=None, input_message_content=None):
        super().__init__('mpeg4_gif', id_, reply_markup)

        self.mpeg4_file_id = mpeg4_file_id
        self.title = title
        self.caption = caption
        self.input_message_content = None

        if input_message_content:
            self.input_message_content = input_message_content.to_dict()
