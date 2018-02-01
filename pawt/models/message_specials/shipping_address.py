from ..base import PAWTBase


class ShippingAddress(PAWTBase):
    def __init__(self, tg, data):
        super().__init__(tg)
        self.country_code = data['country_code']
        self.state = data.get('state')
        self.city = data['city']
        self.street_line1 = data['street_line1']
        self.street_line2 = data.get('street_line2')
        self.post_code = data['post_code']

    def __str__(self):
        return '{l1}{opt_l2}\n{city}{opt_state} {post_code}\n{country}'.format(
            l1=self.street_line1,
            opt_l2=('\n' + self.street_line2) if self.street_line2 else '',
            city=self.city,
            opt_state=(', ' + self.state) if self.state else '',
            post_code=self.post_code,
            country=self.country_code
        )
