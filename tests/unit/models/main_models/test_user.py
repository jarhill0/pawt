from pawt import Telegram
from pawt.models import User


def test_attrs():
    user = User(None, 12345)
    other_user = User(None, dict(id=12345, is_bot=True, first_name="Johnny"))
    for attr in (
        "id",
        "is_bot",
        "first_name",
        "last_name",
        "username",
        "language_code",
    ):
        assert hasattr(user, attr)
        assert hasattr(other_user, attr)


def test_repr():
    user = User(None, 12345)
    assert repr(user) == "<User 12345>"


def test_str():
    data = dict(id=12345, is_bot=True, first_name="Johnny")
    user = User(None, data=data)
    assert str(user) == "Johnny"
    data["last_name"] = "B. Goode"
    user = User(None, data=data)
    assert str(user) == "Johnny B. Goode"
    user = User(None, 12345)
    assert str(user) == ""


def test_eq():
    user1 = User(None, 12345)
    user2 = User(None, "12345")
    user3 = User(None, data=dict(id=12345, is_bot=True, first_name="Johnny"))
    user4 = User(None, 67890)

    assert user1 == user1
    assert user1 == user2
    assert user1 == user3
    assert user3 == user2
    assert user1 != user4

    assert user1 == 12345 == user2
    assert user1 == "12345" == user2
    assert user3 == 12345
    assert user3 == "12345"


def test_chat():
    user = User(Telegram(""), 12345)
    assert user.chat == 12345
