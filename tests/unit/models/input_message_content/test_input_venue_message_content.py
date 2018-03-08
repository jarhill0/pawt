from pawt.models.input_message_content import InputVenueMessageContent as IVMC


def test_input_venue_message_content():
    data = {'latitude': 47.6205978, 'longitude': -122.34952,
            'title': 'Space Needle',
            'address': '400 Broad St, Seattle, WA 98109'}
    assert data == IVMC(**data).to_dict()

    data['foursquare_id'] = 'abc123'
    assert data == IVMC(**data).to_dict()
