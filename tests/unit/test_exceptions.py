from pawt.exceptions import *


def test_api_exception():
    data = {'error_code': 404, 'description': 'That chat has moved',
            'parameters': {'migrate_to_chat_id': 1234}}
    try:
        raise APIException(data)
    except APIException as e:
        assert '400' in str(e)
        assert 'That chat has moved' in str(e)
        assert e.response_parameters == {'migrate_to_chat_id': 1234}
