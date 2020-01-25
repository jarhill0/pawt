from pawt.models.input_message_content import InputContactMessageContent as ICMC


def test_input_contact_message_content():
    data = {"phone_number": "+15555555555", "first_name": "John"}
    assert data == ICMC(**data).to_dict()

    data["last_name"] = "Appleseed"
    assert data == ICMC(**data).to_dict()
