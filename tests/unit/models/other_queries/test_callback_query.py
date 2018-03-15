from pawt import Telegram
from pawt.models.other_queries import CallbackQuery

data = {'id': 'abc123', 'from': {'id': 123456789, 'is_bot': False,
                                 'first_name': 'Sally'},
        'chat_instance': 'def456',
        'data': 'ghi789', 'inline_message_id': '1234567'}
dummy_tg = Telegram('')


def test_callback_query():
    cq = CallbackQuery(dummy_tg, data)
    assert cq.id == 'abc123'
    assert cq.user == 123456789
    assert cq.from_ == 123456789
    assert cq.chat_instance == 'def456'
    assert cq.data == 'ghi789'
    assert repr(cq) == '<CallbackQuery abc123>'
    assert '1234567' == str(cq.inline_message.id)

    for known_attr in ('id', 'user', 'from_', 'message', 'inline_message',
                       'chat_instance', 'data', 'game_short_name'):
        assert hasattr(cq, known_attr)
