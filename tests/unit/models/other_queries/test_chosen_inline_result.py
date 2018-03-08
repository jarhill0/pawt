from pawt import Telegram
from pawt.models.other_queries import ChosenInlineResult

data = {'result_id': 'abc123', 'from': {'id': 123456789, 'is_bot': False,
                                        'first_name': 'Sally'},
        'query': 'testing 1234'}
dummy_tg = Telegram('')


def test_chosen_inline_result():
    cir = ChosenInlineResult(dummy_tg, data)
    assert cir.id == 'abc123'
    assert cir.result_id == 'abc123'
    assert cir.user == 123456789
    assert cir.from_ == 123456789
    assert cir.query == 'testing 1234'
    assert repr(cir) == '<ChosenInlineResult abc123>'

    for known_attr in ('id', 'result_id', 'user', 'from_', 'location',
                       'inline_message', 'query'):
        assert hasattr(cir, known_attr)
