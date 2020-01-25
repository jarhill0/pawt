from ... import bm, tg, user

chat = tg.chat(user)


def get_video_note():
    import os

    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, "video_note_with_sound.mp4")


def test_send():
    with bm.use_cassette("test_video_note__test_send"):
        with open(get_video_note(), "rb") as vid:
            video_note = chat.send_video_note(vid).video_note
        assert video_note == video_note.send(chat).video_note
