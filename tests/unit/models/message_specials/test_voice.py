from pawt import Telegram
from pawt.models.message_specials import Voice

dummy_tg = Telegram(token="")
dummy_data = {"file_id": "abc123", "duration": 65}


def test_attrs():
    v = Voice(dummy_tg, dummy_data)
    assert v.file.id == "abc123"
    assert repr(v) == "<Voice abc123>"

    for known_attr in ("file", "duration", "mime_type"):
        assert hasattr(v, known_attr)
