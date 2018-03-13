from ... import bm, tg, user

chat = tg.chat(user)


def test_send():
    with bm.use_cassette('test_video__test_send'):
        with open(get_video(), 'rb') as vid:
            video = chat.send_video(vid).video
        assert video == video.send(chat).video


def get_video():
    import os
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, 'video_with_sound.mp4')
