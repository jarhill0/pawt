from pawt.models.input_message_content import InputTextMessageContent as ITMC


def test_input_text_message_content():
    data = {"message_text": "Hello World"}
    assert data == ITMC(**data).to_dict()

    data["parse_mode"] = "Markdown"
    assert data == ITMC(**data).to_dict()

    data["disable_web_page_preview"] = True
    assert data == ITMC(**data).to_dict()

    data["disable_web_page_preview"] = False
    assert data == ITMC(**data).to_dict(), "False value should be included"
