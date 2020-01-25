from pawt import Telegram
from pawt.models.message_specials import Audio

dummy_tg = Telegram(token="")
dummy_data = {"file_id": "abc123", "duration": 194}


def test_attrs():
    a = Audio(dummy_tg, dummy_data)
    assert a.file.id == "abc123"
    assert repr(a) == "<Audio abc123>"
    assert a.duration == 194

    for known_attr in (
        "file",
        "file_size",
        "duration",
        "performer",
        "title",
        "mime_type",
    ):
        assert hasattr(a, known_attr)
