from pawt.models.other_queries import InlineMessage

dummy_tg = None


def test_inline_message():
    im = InlineMessage(dummy_tg, "a1234567")
    assert im.id == "a1234567"
