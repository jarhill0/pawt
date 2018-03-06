from pawt import Telegram
from pawt.models.message_specials import Game

dummy_tg = Telegram(token='')
dummy_data = {'title': 'Fun Game', 'description': 'A fun game!',
              'photo': [{'width': 400, 'height': 600, 'file_id': 'abc123'}]}


def test_attrs():
    g = Game(dummy_tg, dummy_data)
    assert g.title == 'Fun Game'
    assert g.description == 'A fun game!'
    assert g.photo[0].width == 400
    assert repr(g) == "<Game 'Fun Game'>"
    assert str(g) == 'Fun Game'

    for known_attr in ('title', 'description', 'photo', 'text',
                       'text_entities', 'animation'):
        assert hasattr(g, known_attr)
