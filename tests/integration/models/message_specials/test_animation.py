from ... import bm, tg, user, game

chat = tg.chat(user)


def test_animation():
    with bm.use_cassette("test_animation__test_animation"):
        message = chat.send_game(game)
        animation = message.game.animation
        assert animation.thumb
