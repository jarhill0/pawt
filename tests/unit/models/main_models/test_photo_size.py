from pawt import Telegram
from pawt.models import PhotoSize

TG = Telegram('')
DICT_1 = dict(file_id=12345, width=640, height=999)
DICT_2 = dict(file_id=12345, width=640, height=999, file_size=123)


def test_diction():
    assert DICT_1 == PhotoSize(TG, DICT_1).to_dict()
    assert DICT_2 == PhotoSize(TG, DICT_2).to_dict()


def test_eq():
    ps1 = PhotoSize(TG, DICT_1)
    ps2 = PhotoSize(TG, DICT_2)
    same_size = PhotoSize(TG, dict(file_id=67890, width=640, height=999))

    assert ps1 == ps1
    assert ps1 == ps2
    assert ps1 != same_size
    assert ps2 != same_size


def test_gt():
    ps1 = PhotoSize(TG, DICT_1)
    bigger = PhotoSize(TG, dict(file_id=1, width=641, height=1000))

    assert bigger > ps1
