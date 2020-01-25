from pawt.models.reply_markup import InlineKeyboardMarkupBuilder
from ... import bm, tg, user

chat = tg.chat(user)


def get_cq(data):
    i = 0
    # get the update for this callbackquery
    while True:
        uds = tg.get_updates(
            allowed_updates=("callback_query",), timeout=20, offset=i + 1
        )
        for ud in uds:
            i = max(i, ud.id)
            if ud.callback_query and ud.callback_query.data == data:
                return ud.callback_query


def test_answer_text():
    builder = InlineKeyboardMarkupBuilder()
    data = "a"
    builder.add_button(text="Press me", callback_data=data)
    with bm.use_cassette("test_callback_query__test_answer_text"):
        chat.send_message("Hello there.", reply_markup=builder.build())
        cq = get_cq(data)
        assert cq.answer("Answered.", show_alert=True, cache_time=1)


def test_answer_url():
    builder = InlineKeyboardMarkupBuilder()
    data = "1"
    builder.add_button(text="Press me for url", callback_data=data)
    with bm.use_cassette("test_callback_query__test_answer_url"):
        un = tg.get_me().username
        link = "https://t.me/{}?start=test_answer_url".format(un)
        chat.send_message("Hello there for url.", reply_markup=builder.build())
        cq = get_cq(data)
        assert cq.answer(url=link, cache_time=1)
