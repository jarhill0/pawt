from pawt.models.input_message_content import InputLocationMessageContent as ILMC


def test_input_location_message_content():
    data = {"latitude": 47.6205978, "longitude": -122.34952}
    assert data == ILMC(**data).to_dict()

    data["live_period"] = 125
    assert data == ILMC(**data).to_dict()
