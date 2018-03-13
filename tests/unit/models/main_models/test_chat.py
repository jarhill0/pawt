from pawt.exceptions import BadArgument
from pawt.models import Chat
from pawt.models.main_models.chat import make_labeled_price

ID = '12345'
DUMMY_TG = None
DUMMY_DATA = dict(id=ID, type='private')


def test_creation():
    chat = Chat(DUMMY_TG, ID)
    assert chat.id == ID

    chat = Chat(DUMMY_TG, chat_id=ID)
    assert chat.id == ID


def test_num_args():
    # improper creation
    try:
        Chat(DUMMY_TG)
    except BadArgument:
        pass
    else:
        assert False

    try:
        Chat(DUMMY_TG, ID, DUMMY_DATA)
    except BadArgument:
        pass
    else:
        assert False

    try:
        Chat(DUMMY_TG, ID, data=DUMMY_DATA)
    except BadArgument:
        pass
    else:
        assert False

    try:
        Chat(DUMMY_TG, chat_id=ID, data=DUMMY_DATA)
    except BadArgument:
        pass
    else:
        assert False

    # proper creation
    chat = Chat(DUMMY_TG, ID)
    chat = Chat(DUMMY_TG, chat_id=ID)
    chat = Chat(DUMMY_TG, data=DUMMY_DATA)


def test_str():
    dummy_data = DUMMY_DATA.copy()
    title = 'My Title'
    dummy_data['title'] = title

    chat = Chat(DUMMY_TG, data=dummy_data)
    assert str(chat) == title

    dummy_data['title'] = None

    chat = Chat(DUMMY_TG, data=dummy_data)
    assert str(chat) == str(ID)


def test_repr():
    chat = Chat(DUMMY_TG, ID)
    assert repr(chat) == '<Chat 12345>'


def test_equality():
    pass  # make sure to test across data/chat_id creations
    chat = Chat(DUMMY_TG, ID)

    assert chat == chat
    assert chat == ID
    assert chat == str(ID)
    assert chat == int(ID)

    other_chat = Chat(DUMMY_TG, data=DUMMY_DATA)
    assert other_chat == other_chat
    assert other_chat == ID
    assert other_chat == str(ID)
    assert other_chat == int(ID)

    assert chat == other_chat

    assert chat != '123456'
    assert chat != Chat(DUMMY_TG, '123456')

    dummy_data = DUMMY_DATA.copy()
    dummy_data['title'] = 'My Title'

    assert chat == Chat(DUMMY_TG, data=dummy_data)

    dummy_data['title'] = '12345'
    dummy_data['id'] = '54321'

    assert chat != Chat(DUMMY_TG, data=dummy_data)


def test_labeled_price():
    expected = {'label': 'USD',
                'amount': 399}
    assert make_labeled_price('USD', 399) == expected


def test_media_group_limits():
    try:
        Chat(DUMMY_TG, DUMMY_DATA).send_media_group([5])
        assert False, 'should raise BadArgument'
    except BadArgument:
        pass

    try:
        Chat(DUMMY_TG, DUMMY_DATA).send_media_group([5] * 11)
        assert False, 'should raise BadArgument'
    except BadArgument:
        pass
