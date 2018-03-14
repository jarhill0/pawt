from pawt import Telegram
from pawt.models.inline_queries import InlineQuery

dummy_tg = Telegram('')
data = {'id': 'abc123', 'query': 'kittens', 'offset': 3,
        'from': {'id': 123456789,
                 'is_bot': False,
                 'first_name': 'Sally'}}
location = {'latitude': 37.872059, 'longitude': -122.257812}


def test_inline_query():
    iq = InlineQuery(dummy_tg, data)

    assert iq.id == 'abc123'
    assert iq.query == 'kittens'
    assert iq.offset == 3
    assert iq.user == 123456789
    assert iq.from_ == 123456789
    assert repr(iq) == '<InlineQuery abc123>'
    assert str(iq) == 'kittens'

    for known_attr in ('id', 'user', 'from_', 'query', 'offset', 'location'):
        assert hasattr(iq, known_attr)

    data['location'] = location
    iq = InlineQuery(dummy_tg, data)
    assert iq.location.latitude == 37.872059
