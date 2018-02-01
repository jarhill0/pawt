from .inline_query_result import InlineQueryResult


class InlineQueryResultArticle(InlineQueryResult):
    """Represents a link to an article or web page."""

    def __init__(self, id_, title, input_message_content,
                 reply_markup=None, url=None, hide_url=None, description=None,
                 thumb_url=None, thumb_width=None, thumb_height=None):
        super().__init__('article', id_, reply_markup)

        self.title = title
        self.input_message_content = input_message_content.to_dict()
        self.url = url
        self.hide_url = hide_url
        self.description = description
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
