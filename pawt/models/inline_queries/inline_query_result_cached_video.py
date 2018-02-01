from .inline_query_result import InlineQueryResult


class InlineQueryResultCachedVideo(InlineQueryResult):
    """Represents a link to a video file stored on the Telegram servers. By
    default, this video file will be sent by the user with an optional caption.
    Alternatively, you can use input_message_content to send a message with the
    specified content instead of the video."""

    def __init__(self, id_, video_file_id, title, description=None,
                 caption=None, reply_markup=None, input_message_content=None):
        super().__init__('video', id_, reply_markup)

        self.video_file_id = video_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.input_message_content = input_message_content.to_dict()
