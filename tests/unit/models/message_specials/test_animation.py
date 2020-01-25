from pawt import Telegram
from pawt.models.message_specials import Animation

dummy_tg = Telegram(token="")
dummy_data = {"file_id": "abc123", "file_name": "My animation.mp4"}


def test_attrs():
    a = Animation(dummy_tg, dummy_data)
    assert a.file.id == "abc123"
    assert repr(a) == "<Animation abc123>"
    assert a.file_name == "My animation.mp4"

    for known_attr in ("file", "file_size", "file_name", "mime_type", "thumb"):
        assert hasattr(a, known_attr)
