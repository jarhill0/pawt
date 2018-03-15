from json import dumps

from pawt.exceptions import BadArgument
from ..base import PAWTBase
from ..message_specials import ShippingAddress
from ...const import API_PATH


class ShippingQuery(PAWTBase):
    @staticmethod
    def make_labeled_price(label, amount):
        return dict(label=label, amount=amount)

    @staticmethod
    def make_shipping_option(id_, title, prices):
        return dict(id=id_, title=title, prices=prices)

    def __init__(self, tg, data):
        super().__init__(tg)

        self.id = data['id']
        self.user = tg.user(data=data['from'])
        self.from_ = self.user
        self.invoice_payload = data['invoice_payload']
        self.shipping_address = ShippingAddress(tg, data['shipping_address'])

    def __repr__(self):
        return '<ShippingQuery {}>'.format(self.id)

    def answer(self, ok, shipping_options=None, error_message=None):
        if not (bool(shipping_options) == bool(ok) != bool(error_message)):
            raise BadArgument('shipping_options only must be provided if ok, '
                              'otherwise error_message only')
        info = dict(shipping_query_id=self.id, ok=ok)
        if ok:
            info['shipping_options'] = dumps(shipping_options)
        else:
            info['error_message'] = error_message
        return self._tg.post(API_PATH['answer_shipping_query'], data=info)
