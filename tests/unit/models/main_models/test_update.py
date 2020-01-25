from pawt.models import Update


def test_repr():
    up = Update(None, data=dict(update_id=12))
    assert repr(up) == "<Update 12>"


def test_str():
    # in reality, content and content_type will never be None
    up = Update(None, data=dict(update_id=12))
    assert str(up) == "None None"
