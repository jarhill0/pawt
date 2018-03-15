from pawt import Telegram
from pawt.exceptions import BadArgument
from pawt.models.other_queries import ShippingQuery

data = {'id': 'abc123', 'invoice_payload': 'def456',
        'from': {'id': 123456789, 'is_bot': False,
                 'first_name': 'Sally'},
        'shipping_address': {'country_code': 'USA',
                             'state': 'CA',
                             'city': 'San Francisco',
                             'street_line1': '1 Telegraph Hill Blvd',
                             'post_code': '94133'}
        }
dummy_tg = Telegram('')


def test_attrs():
    sq = ShippingQuery(dummy_tg, data)
    assert sq.id == 'abc123'
    assert sq.user == 123456789
    assert sq.from_ == 123456789
    assert sq.invoice_payload == 'def456'

    assert repr(sq) == '<ShippingQuery abc123>'

    for known_attr in ('id', 'user', 'from_', 'invoice_payload',
                       'shipping_address'):
        assert hasattr(sq, known_attr)


def test_answer_validation():
    sq = ShippingQuery(dummy_tg, data)

    try:
        sq.answer(True)
        assert False, 'should raise BadArgument'
    except BadArgument:
        pass

    try:
        sq.answer(False)
        assert False, 'should raise BadArgument'
    except BadArgument:
        pass

    try:
        sq.answer(True, [12], 'everything went right')
        assert False, 'should raise BadArgument'
    except BadArgument:
        pass

    try:
        sq.answer(False, [9999], 'everything went wrong')
        assert False, 'should raise BadArgument'
    except BadArgument:
        pass


def test_make_labeled_price():
    expected = {'label': 'Free', 'amount': 0}
    out = ShippingQuery.make_labeled_price('Free', 0)
    assert out == expected


def test_make_shipping_option():
    expected = {'id': 'abc123', 'title': 'Options', 'prices': []}
    out = ShippingQuery.make_shipping_option('abc123', 'Options', [])
    assert out == expected
