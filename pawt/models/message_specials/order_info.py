from .shipping_address import ShippingAddress
from ..base import PAWTBase


class OrderInfo(PAWTBase):
    def __init__(self, tg, data):
        super().__init__(tg)

        self.name = data.get('name')
        self.phone_number = data.get('phone_number')
        self.email = data.get('email')

        if data.get('shipping_address'):
            self.shipping_address = ShippingAddress(
                tg, data=data['shipping_address'])
        else:
            self.shipping_address = None
