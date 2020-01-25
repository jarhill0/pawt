from pawt.models.message_specials import Location

dummy_tg = None
dummy_data = {"latitude": 37.872059, "longitude": -122.257812}


def test_attrs():
    l = Location(dummy_tg, dummy_data)
    assert l.latitude == 37.872059
    assert l.longitude == -122.257812
    assert repr(l) == "<Location (37.872059, -122.257812)>"
    assert str(l) == "(37.872059, -122.257812)"
