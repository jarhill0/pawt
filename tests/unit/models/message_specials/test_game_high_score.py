from pawt import Telegram
from pawt.models.message_specials import GameHighScore

dummy_tg = Telegram(token="")
dummy_data = {
    "position": 2,
    "score": 100,
    "user": {
        "id": 123456789,
        "is_bot": False,
        "first_name": "Jack",
        "last_name": "Rabbit",
    },
}


def test_attrs():
    ghs = GameHighScore(dummy_tg, dummy_data)
    assert ghs.position == 2
    assert ghs.score == 100
    assert repr(ghs) == "<GameHighScore for <User 123456789>>"
    assert str(ghs) == "#2: Jack Rabbit got 100 points"

    for known_attr in ("user", "position", "score"):
        assert hasattr(ghs, known_attr)
