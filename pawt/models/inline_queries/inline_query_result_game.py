from .inline_query_result import InlineQueryResult


class InlineQueryResultGame(InlineQueryResult):
    """Represents a Game."""

    def __init__(self, id_, game_short_name, reply_markup=None):
        super().__init__('game', id_, reply_markup)

        self.game_short_name = game_short_name
