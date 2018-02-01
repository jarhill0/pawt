from .inline_query_result import InlineQueryResult


class InlineQueryResultVideo(InlineQueryResult):
    """Represents a link to a page containing an embedded video player or a
    video file. By default, this video file will be sent by the user with an
    optional caption. Alternatively, you can use input_message_content to
    send a message with the specified content instead of the video.If an
    InlineQueryResultVideo message contains an embedded video (e.g., YouTube),
    you must replace its content using input_message_content."""

    def __init__(self, id_, video_url, mime_type, thumb_url, title,
                 caption=None, video_width=None, video_height=None,
                 video_duration=None, description=None, reply_markup=None,
                 input_message_content=None):
        super().__init__('video', id_, reply_markup)

        self.video_url = video_url
        self.mime_type = mime_type
        self.thumb_url = thumb_url
        self.title = title
        self.caption = caption
        self.video_width = video_width
        self.video_height = video_height
        self.video_duration = video_duration
        self.description = description
        self.input_message_content = input_message_content.to_dict()
