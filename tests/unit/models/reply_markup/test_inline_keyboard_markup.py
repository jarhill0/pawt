from pawt.exceptions import BadArgument
from pawt.models.reply_markup import InlineKeyboardMarkupBuilder, callback_game

EXPECTED = {
    "inline_keyboard": [
        [
            {"text": "click on this url", "url": "https://duckduckgo.com"},
            {"text": "call me back, Data", "callback_data": "abc123"},
            {"text": "Nintendo Switch", "switch_inline_query": "Nintendo"},
        ],
        [
            {
                "text": "Switch here",
                "switch_inline_query_current_chat": "swotched here",
            },
            {"text": "Cool game", "callback_game": {}},
            {"text": "Don't pay", "pay": False},
        ],
    ]
}


def test_building():
    builder = InlineKeyboardMarkupBuilder()
    builder.add_button("click on this url", url="https://duckduckgo.com")
    builder.add_button("call me back, Data", callback_data="abc123")
    builder.add_button("Nintendo Switch", switch_inline_query="Nintendo")
    builder.new_row()
    builder.add_button("Switch here", switch_inline_query_current_chat="swotched here")
    builder.add_button("Cool game", callback_game=callback_game())
    builder.add_button("Don't pay", pay=False)

    assert EXPECTED == builder.build()


def test_num_args():
    builder = InlineKeyboardMarkupBuilder()
    try:
        builder.add_button("hello")
        assert False
    except BadArgument:
        pass

    try:
        builder.add_button("hello", url="python.org", pay=True)
        assert False
    except BadArgument:
        pass
