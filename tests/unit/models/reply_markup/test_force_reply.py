from pawt.models.reply_markup import force_reply


def test_output():
    assert force_reply() == {"force_reply": True}
    assert force_reply(True) == {"force_reply": True, "selective": True}
    assert force_reply(False) == {"force_reply": True, "selective": False}
