from .inline_query_result import InlineQueryResult


class InlineQueryResultLocation(InlineQueryResult):
    """Represents a location on a map. By default, the location will be sent
    by the user. Alternatively, you can use input_message_content to send a
    message with the specified content instead of the location."""

    def __init__(self, id_, latitude, longitude, title, live_period=None,
                 reply_markup=None, input_message_content=None, thumb_url=None,
                 thumb_width=None, thumb_height=None):
        super().__init__('location', id_, reply_markup)

        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.live_period = live_period
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        self.input_message_content = None

        if input_message_content:
            self.input_message_content = input_message_content.to_dict()
