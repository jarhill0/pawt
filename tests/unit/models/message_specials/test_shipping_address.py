from pawt.models.message_specials import ShippingAddress

dummy_tg = None
dummy_data = {'country_code': 'USA',
              'state': 'CA',
              'city': 'San Francisco',
              'street_line1': '1 Telegraph Hill Blvd',
              'post_code': '94133'}


def test_attrs():
    sa = ShippingAddress(dummy_tg, dummy_data)
    assert sa.country_code == 'USA'
    assert sa.state == 'CA'
    assert sa.city == 'San Francisco'
    assert sa.street_line1 == '1 Telegraph Hill Blvd'
    assert sa.post_code == '94133'
    assert str(sa) == '1 Telegraph Hill Blvd\nSan Francisco, CA 94133\nUSA'

    for known_attr in ('country_code', 'state', 'city', 'street_line1',
                       'street_line2', 'post_code'):
        assert hasattr(sa, known_attr)
