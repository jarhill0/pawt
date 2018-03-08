from pawt import Telegram
from pawt.models.message_specials import Video

dummy_tg = Telegram(token='')
dummy_data = {'file_id': 'abc123', 'width': 400, 'height': 600, 'duration': 60}


def test_attrs():
    v = Video(dummy_tg, dummy_data)
    assert v.file.id == 'abc123'
    assert v.width == 400
    assert v.height == 600
    assert v.duration == 60
    assert repr(v) == '<Video abc123>'

    for known_attr in ('file', 'width', 'height', 'duration', 'mime_type',
                       'thumb'):
        assert hasattr(v, known_attr)
