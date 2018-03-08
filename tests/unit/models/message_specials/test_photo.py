from pawt import Telegram
from pawt.models.message_specials import Photo

dummy_tg = Telegram(token='')
dummy_data = [
    {'file_id': 1, 'width': 200, 'height': 400},
    {'file_id': 2, 'width': 400, 'height': 800},
    {'file_id': 3, 'width': 800, 'height': 1600}
]


def test_attrs():
    p = Photo(dummy_tg, dummy_data)
    assert p[2] > p[1] > p[0]
    assert p.max_size.file.id == 3
    assert p.min_size.file.id == 1
    assert repr(p) == '<Photo (3 sizes)>'
