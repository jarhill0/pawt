from pawt.exceptions import TooLong
from . import bm, tg, user

chat = tg.chat(user)

pic = (
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Tursiops_"
    "truncatus_01.jpg/800px-Tursiops_truncatus_01.jpg"
)


def check_text(messages, text):
    return (
        text.strip() == " ".join(m.text for m in messages).strip()
        or text.strip() == "".join(m.text for m in messages).strip()
    )


def test_toolong_with_caption():
    captions = ["I am " * 100, "B" * 500]
    with bm.use_cassette("test_exceptions__test_toolong_with_caption"):
        for caption in captions:
            try:
                chat.send_photo(pic, caption)
                assert False, "should raise Toolong"
            except TooLong as tl:
                messages = tl.send_chunked()
                sent_opt_1 = " ".join(m.caption for m in messages)
                sent_opt_2 = "".join(m.caption for m in messages)
                assert (
                    caption.strip() == sent_opt_1.strip()
                    or caption.strip() == sent_opt_2.strip()
                )


def test_toolong_with_spaces():
    message = "Hello world! " * 316
    with bm.use_cassette("test_exceptions__test_toolong_with_spaces"):
        try:
            chat.send_message(message)
            assert False, "should raise TooLong"
        except TooLong as tl:
            assert check_text(tl.send_chunked(), message)


def test_toolong_without_spaces():
    message = "a" * 5000
    with bm.use_cassette("test_exceptions__test_toolong_without_spaces"):
        try:
            chat.send_message(message)
            assert False, "should raise TooLong"
        except TooLong as tl:
            assert check_text(tl.send_chunked(), message)


def test_one_under_limit():
    message = "Hello world! " * 315
    with bm.use_cassette("test_exceptions__test_one_under_limit"):
        assert chat.send_message(message)


def test_limit_exactly():
    message = "Hello world! " * 315 + "H"
    with bm.use_cassette("test_exceptions__test_limit_exactly"):
        assert chat.send_message(message)


def test_one_over_limit():
    message = "Hello world! " * 315 + "He"
    with bm.use_cassette("test_exceptions__test_one_over_limit"):
        try:
            chat.send_message(message)
            assert False, "should raise TooLong"
        except TooLong as tl:
            assert check_text(tl.send_chunked(), message)
