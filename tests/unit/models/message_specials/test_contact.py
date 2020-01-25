from pawt import Telegram
from pawt.exceptions import BadArgument
from pawt.models import User
from pawt.models.message_specials import Contact

dummy_tg = Telegram(token="")
dummy_data = {"phone_number": "+15555555555", "first_name": "Jack"}


def test_attrs():
    c = Contact(dummy_tg, dummy_data)
    assert c.phone_number == "+15555555555"
    assert repr(c) == "<Contact +15555555555>"

    for known_attr in ("phone_number", "first_name", "last_name", "user_id"):
        assert hasattr(c, known_attr)


def test_str():
    data = dummy_data.copy()
    c = Contact(dummy_tg, data)
    assert str(c) == "Jack"
    data["last_name"] = "Rabbit"
    c = Contact(dummy_tg, data)
    assert str(c) == "Jack Rabbit"


def test_to_user():
    data = dummy_data.copy()
    try:
        Contact(dummy_tg, data).to_user()
    except BadArgument:
        pass
    else:
        assert False, "BadArgument not thrown"
    data["user_id"] = 123456789
    c = Contact(dummy_tg, data)
    u = c.to_user()
    assert isinstance(u, User)
    assert u == 123456789
    assert c.user_id == 123456789
    assert c != u


def test_eq():
    # different phone numbers
    assert Contact(None, {"phone_number": "123", "first_name": "Jack"}) != Contact(
        None, {"phone_number": "7", "first_name": "Jack"}
    )

    # different first names
    assert Contact(None, {"phone_number": "123", "first_name": "Jack"}) != Contact(
        None, {"phone_number": "123", "first_name": "John"}
    )

    # same num and first name
    assert Contact(None, {"phone_number": "123", "first_name": "Jack"}) == Contact(
        None, {"phone_number": "123", "first_name": "Jack"}
    )

    # one missing last name
    assert Contact(
        None, {"phone_number": "123", "first_name": "Jack", "last_name": "Jackson"}
    ) != Contact(None, {"phone_number": "123", "first_name": "Jack"})

    # same num, first name, last name
    assert Contact(
        None, {"phone_number": "123", "first_name": "Jack", "last_name": "Jackson"}
    ) == Contact(
        None, {"phone_number": "123", "first_name": "Jack", "last_name": "Jackson"}
    )
