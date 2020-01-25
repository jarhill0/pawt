from pawt import Telegram
from pawt.models.message_specials import Document

dummy_tg = Telegram(token="")
dummy_data = {"file_id": "abc123"}


def test_attrs():
    d = Document(dummy_tg, dummy_data)
    assert d.file.id == "abc123"
    assert repr(d) == "<Document abc123>"

    for known_attr in ("file", "file_size", "file_name", "mime_type", "thumb"):
        assert hasattr(d, known_attr)
