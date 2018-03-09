from .inline_query_result import InlineQueryResult


class InlineQueryResultVenue(InlineQueryResult):
    """Represents a venue. By default, the venue will be sent by the user.
    Alternatively, you can use input_message_content to send a message with
    the specified content instead of the venue."""

    def __init__(self, id_, latitude, longitude, title, address,
                 foursquare_id=None, reply_markup=None,
                 input_message_content=None, thumb_url=None, thumb_width=None,
                 thumb_height=None):
        super().__init__('venue', id_, reply_markup)

        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        self.input_message_content = None

        if input_message_content:
            self.input_message_content = input_message_content.to_dict()
