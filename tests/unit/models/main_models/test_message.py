from pawt.exceptions import BadArgument
from pawt.models import Message
from pawt.telegram import Telegram

TG = Telegram("")
DUMMY_DATA = dict(
    message_id=12345, date=1234567890, chat=dict(id=67890, type="private")
)


def test_creation():
    message = Message(TG, DUMMY_DATA)
    assert repr(message) == "<Message 12345>"


def test_from():
    dummy_data = DUMMY_DATA.copy()
    dummy_data["from"] = dict(id=17, is_bot=False, first_name="Johnny")
    message = Message(TG, dummy_data)
    assert message.from_ == message.user == 17


def test_content():
    dummy_data = DUMMY_DATA.copy()
    assert Message(TG, dummy_data).get_text_content() == ""
    dummy_data["caption"] = "My Caption"
    assert Message(TG, dummy_data).get_text_content() == "My Caption"
    dummy_data["text"] = "My Text"
    assert Message(TG, dummy_data).get_text_content() == "My Text"


def test_empty_edit():
    dummy_data = DUMMY_DATA.copy()
    dummy_data["text"] = "My Text"
    message = Message(TG, dummy_data)
    try:
        message.edit()
        assert False, "should raise BadArgument"
    except BadArgument:
        pass
