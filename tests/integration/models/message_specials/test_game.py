from ... import bm, game, tg, user

chat = tg.chat(user)


def test_text_entities():
    with bm.use_cassette('test_game__test_text_entities'):
        message = chat.send_game(game)
        assert len(message.game.text_entities) == 0
        message = message.edit('This is a *game*', parse_mode='Markdown')
    assert len(message.game.text_entities) > 0


def test_animation():
    with bm.use_cassette('test_game__test_animation'):
        game_obj = chat.send_game(game).game
    assert game_obj.animation
