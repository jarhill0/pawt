from pawt import Telegram
from pawt.models import ChatPhoto, File

DATA = dict(small_file_id="abcdef123", big_file_id="ghijkl456")
TG = Telegram("")


def test_chat_photo():
    chat_photo = ChatPhoto(TG, data=DATA)
    assert isinstance(chat_photo.small_file, File)
    assert isinstance(chat_photo.big_file, File)
