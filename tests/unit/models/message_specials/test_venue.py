from pawt import Telegram
from pawt.models.message_specials import Venue

dummy_tg = Telegram(token="")
dummy_data = {
    "location": {"latitude": 37.802308, "longitude": -122.405791},
    "title": "Coit Tower",
    "address": "1 Telegraph Hill Blvd, San Francisco, CA 94133",
}


def test_attrs():
    v = Venue(dummy_tg, dummy_data)
    assert v.location.latitude, v.location.longitude == (37.802308, -122.405791)
    assert v.title == "Coit Tower"
    assert v.address == "1 Telegraph Hill Blvd, San Francisco, CA 94133"
    assert repr(v) == "<Venue Coit Tower>"
    assert str(v) == "Coit Tower"

    for known_attr in ("location", "title", "address", "foursquare_id"):
        assert hasattr(v, known_attr)
