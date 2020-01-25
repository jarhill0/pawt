from pawt.models.inline_queries import InlineQueryResultArticle
from pawt.models.input_message_content import InputTextMessageContent
from ... import bm, tg

dummy_query = {
    "from": {
        "first_name": "J",
        "id": 329098275,
        "is_bot": False,
        "language_code": "en-US",
        "last_name": "R",
        "username": "jarhill0",
    },
    "id": "1413466331253702152",
    "offset": "",
    "query": "Hello friend",
}


def test_respond():
    input_content = InputTextMessageContent(
        "[Stephen Hawking: Visionary "
        "physicist dies aged 76]("
        "http://www.bbc.com/news/"
        "uk-43396008)",
        parse_mode="Markdown",
    )
    article = InlineQueryResultArticle(
        "a",
        "Stephen Hawking: Visionary " "physicist dies aged 76",
        input_content,
        url="http://www.bbc.com/" "news/uk-43396008",
    )
    with bm.use_cassette("test_inline_query__test_respond"):
        while True:
            updates = tg.get_updates(allowed_updates=("inline_query",))
            if updates:
                iq = updates[-1].inline_query
                break

        iq.answer(
            [article],
            cache_time=400,
            is_personal=True,
            next_offset="2",
            switch_pm_text="Read more",
            switch_pm_parameter="Hawking",
        )
