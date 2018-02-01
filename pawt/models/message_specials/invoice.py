from .util import format_currency
from ..base import PAWTBase


class Invoice(PAWTBase):
    def __init__(self, tg, data):
        super().__init__(tg)

        self.title = data['title']
        self.description = data['description']
        self.start_parameter = data['start_parameter']
        self.currency = data['currency']
        self.total_amount = data['total_amount']

    def __repr__(self):
        return '<Invoice {}>'.format(self.title)

    def __str__(self):
        return '{} ({})'.format(self.title, self.format_cost())

    def format_cost(self):
        return format_currency(self.currency, self.total_amount, self._tg)
