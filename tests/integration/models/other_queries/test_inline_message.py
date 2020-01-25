from pawt.models.inline_queries import (
    InlineQueryResultArticle,
    InlineQueryResultLocation,
    InlineQueryResultPhoto,
)
from pawt.models.input_message_content import InputTextMessageContent
from pawt.models.reply_markup import InlineKeyboardMarkupBuilder
from ... import bm, tg, user

builder = InlineKeyboardMarkupBuilder()
builder.add_button(text="Don't press me", callback_data="Nothing, yo")
input_content = InputTextMessageContent(
    "[Stephen Hawking: Visionary "
    "physicist dies aged 76]("
    "http://www.bbc.com/news/"
    "uk-43396008)",
    parse_mode="Markdown",
)
article = InlineQueryResultArticle(
    "abc123",
    "Stephen Hawking: Visionary " "physicist dies aged 76",
    input_content,
    url="http://www.bbc.com/" "news/uk-43396008",
    reply_markup=builder.build(),
)


def get_inline_query(text):
    i = 0
    while True:
        uds = tg.get_updates(
            allowed_updates=("inline_query",), timeout=20, offset=i + 1
        )
        for ud in uds:
            i = max(i, ud.id)
            if (
                ud.inline_query
                and ud.inline_query.user == user
                and ud.inline_query.query == text
            ):
                return ud.inline_query


def get_chosen_inline_result(id_):
    i = 0
    while True:
        uds = tg.get_updates(
            allowed_updates=("chosen_inline_result",), timeout=20, offset=i + 1
        )
        for ud in uds:
            i = max(i, ud.id)
            if ud.chosen_inline_result and ud.chosen_inline_result.id == id_:
                return ud.chosen_inline_result


def test_edit_text():
    with bm.use_cassette("test_inline_message__test_edit_text"):
        # gotta wait for a query
        iq = get_inline_query("test_edit_text")
        iq.answer([article], cache_time=0)
        builder.new_row()
        builder.add_button("Me neither", callback_data="Nothing also")
        # gotta wait for a choice...
        cir = get_chosen_inline_result("abc123")
        assert cir.inline_message.edit_text(
            "<b>No</b> article for you!",
            reply_markup=builder.build(),
            parse_mode="HTML",
            disable_web_page_preview=True,
        )


URL = (
    "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Frog_in_pond_"
    "0547.jpg/640px-Frog_in_pond_0547.jpg"
)
THUMB = (
    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Frog_in_pon"
    "d_0539.jpg/320px-Frog_in_pond_0539.jpg"
)

photo = InlineQueryResultPhoto(
    "frog",
    photo_url=URL,
    thumb_url=THUMB,
    caption="This is the first caption",
    reply_markup=builder.build(),
)


def test_edit_caption():
    with bm.use_cassette("test_inline_message_test_edit_caption"):
        iq = get_inline_query("test_edit_caption")
        iq.answer([photo], cache_time=0)
        cir = get_chosen_inline_result("frog")
        builder.add_button("Another button", callback_data="skjdfh")
        assert cir.inline_message.edit_caption(
            "This is the second caption", reply_markup=builder.build()
        )


def test_edit_reply_markup():
    with bm.use_cassette("test_inline_message__test_edit_reply_markup"):
        iq = get_inline_query("test_edit_reply_markup")
        iq.answer([article, photo], cache_time=0)
        cir = get_chosen_inline_result("frog")
        builder.new_row()
        builder.add_button("Yet another button", url="ddg.co")
        assert cir.inline_message.edit_reply_markup(reply_markup=builder.build())


location = InlineQueryResultLocation(
    "campanile",
    latitude=37.8720789,
    longitude=-122.258008,
    title="Where I am",
    live_period=65,
    reply_markup=builder.build(),
)


def test_edit_live_location():
    with bm.use_cassette("test_inline_message__test_edit_live_location"):
        iq = get_inline_query("test_edit_live_location")
        iq.answer([location], cache_time=0)
        cir = get_chosen_inline_result("campanile")
        builder.new_row()
        builder.add_button("1", url="ddg.co")
        assert cir.inline_message.edit_live_location(
            47.6205978, -122.34952, reply_markup=builder.build()
        )


location2 = InlineQueryResultLocation(
    "campanile2",
    latitude=37.8720789,
    longitude=-122.258008,
    title="Where I am",
    live_period=65,
    reply_markup=builder.build(),
)


def test_stop_live_location():
    with bm.use_cassette("test_inline_message__test_stop_live_location"):
        iq = get_inline_query("test_stop_live_location")
        iq.answer([location2], cache_time=0)
        cir = get_chosen_inline_result("campanile2")
        builder.add_button("2", url="ddg.co")
        assert cir.inline_message.stop_live_location(builder.build())
