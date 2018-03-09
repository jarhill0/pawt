from .inline_query_result import InlineQueryResult


class InlineQueryResultPhoto(InlineQueryResult):
    """Represents a link to a photo. By default, this photo will be sent by the
    user with optional caption. Alternatively, you can use input_message_content
    to send a message with the specified content instead of the photo."""

    def __init__(self, id_, photo_url, thumb_url, photo_width=None,
                 photo_height=None, title=None, description=None, caption=None,
                 reply_markup=None, input_message_content=None):
        super().__init__('photo', id_, reply_markup)

        self.photo_url = photo_url
        self.thumb_url = thumb_url
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.title = title
        self.description = description
        self.caption = caption
        self.input_message_content = None

        if input_message_content:
            self.input_message_content = input_message_content.to_dict()
