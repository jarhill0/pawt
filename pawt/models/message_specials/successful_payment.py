from .order_info import OrderInfo
from .util import format_currency
from ..base import PAWTBase


class SuccessfulPayment(PAWTBase):
    def __init__(self, tg, data):
        super().__init__(tg)

        self.currency = data['currency']
        self.total_amount = data['total_amount']
        self.invoice_payload = data['invoice_payload']
        self.shipping_option_id = data.get('shipping_option_id')
        self.telegram_payment_charge_id = data['telegram_payment_charge_id']
        self.provider_payment_charge_id = data['provider_payment_charge_id']

        if data.get('order_info'):
            self.order_info = OrderInfo(tg, data['order_info'])
        else:
            self.order_info = None

    def __repr__(self):
        return '<SuccessfulPayment {}>'.format(self.format_cost())

    def format_cost(self):
        return format_currency(self.currency, self.total_amount, self._tg)
