from pawt import Telegram
from pawt.models.message_specials import VideoNote

dummy_tg = Telegram(token='')
dummy_data = {'file_id': 'abc123', 'length': 400, 'duration': 60}


def test_attrs():
    vn = VideoNote(dummy_tg, dummy_data)
    assert vn.file.id == 'abc123'
    assert vn.length == 400
    assert vn.duration == 60
    assert repr(vn) == '<VideoNote abc123>'

    for known_attr in ('file', 'length', 'duration', 'thumb'):
        assert hasattr(vn, known_attr)
