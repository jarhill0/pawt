from pawt import Telegram
from pawt.models.message_specials import FileWrapper

data = {'file_id': 'abc123'}
tg = Telegram('')


def test_file_wrapper_eq():
    assert FileWrapper(tg, data) == FileWrapper(tg, data)
    assert FileWrapper(tg, data) == 'abc123'
    assert FileWrapper(tg, data) != FileWrapper(tg, {'file_id': '123abc'})
