from pawt.models.inline_queries import (InlineQueryResultArticle,
                                        InlineQueryResultAudio,
                                        InlineQueryResultCachedAudio,
                                        InlineQueryResultCachedDocument,
                                        InlineQueryResultCachedGif,
                                        InlineQueryResultCachedMpeg4Gif,
                                        InlineQueryResultCachedPhoto,
                                        InlineQueryResultCachedSticker,
                                        InlineQueryResultCachedVideo,
                                        InlineQueryResultCachedVoice,
                                        InlineQueryResultContact,
                                        InlineQueryResultDocument,
                                        InlineQueryResultGame,
                                        InlineQueryResultGif,
                                        InlineQueryResultLocation,
                                        InlineQueryResultMpeg4Gif,
                                        InlineQueryResultPhoto,
                                        InlineQueryResultVenue,
                                        InlineQueryResultVideo,
                                        InlineQueryResultVoice)
from pawt.models.input_message_content import InputTextMessageContent

INPUT_MESSAGE_CONTENT = InputTextMessageContent('hello')


def test_article():
    data = {'title': 'Hello world!',
            'input_message_content': INPUT_MESSAGE_CONTENT}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'article'
    expected['input_message_content'] = INPUT_MESSAGE_CONTENT.to_dict()
    obj = InlineQueryResultArticle('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultArticle abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'input_message_content',
                       'title', 'url', 'hide_url', 'description', 'thumb_url',
                       'thumb_width', 'thumb_height'):
        assert hasattr(obj, known_attr)


def test_audio():
    data = {'audio_url': 'https://my.site/song.mp3', 'title': 'Hello world!',
            'audio_duration': 300}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'audio'
    obj = InlineQueryResultAudio('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultAudio abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'input_message_content',
                       'title', 'audio_url', 'caption', 'performer',
                       'audio_duration'):
        assert hasattr(obj, known_attr)


def test_cached_audio():
    data = {'audio_file_id': 'def456', 'caption': 'Hello world!'}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'audio'
    obj = InlineQueryResultCachedAudio('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultCachedAudio abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'audio_file_id',
                       'caption', 'input_message_content'):
        assert hasattr(obj, known_attr)


def test_cached_document():
    data = {'title': 'My PDF', 'document_file_id': 'def456',
            'caption': 'Pls read'}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'document'
    obj = InlineQueryResultCachedDocument('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultCachedDocument abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'title',
                       'document_file_id', 'description', 'caption',
                       'input_message_content'):
        assert hasattr(obj, known_attr)


def test_cached_gif():
    data = {'gif_file_id': 'def456', 'caption': 'Pls loop'}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'gif'
    obj = InlineQueryResultCachedGif('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultCachedGif abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'gif_file_id', 'title',
                       'caption', 'input_message_content'):
        assert hasattr(obj, known_attr)


def test_cached_mpeg4_gif():
    data = {'mpeg4_file_id': 'def456', 'caption': 'Pls loop'}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'mpeg4_gif'
    obj = InlineQueryResultCachedMpeg4Gif('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultCachedMpeg4Gif abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'mpeg4_file_id', 'title',
                       'caption', 'input_message_content'):
        assert hasattr(obj, known_attr)


def test_cached_photo():
    data = {'photo_file_id': 'def456', 'caption': 'Pls loop'}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'photo'
    obj = InlineQueryResultCachedPhoto('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultCachedPhoto abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'photo_file_id', 'title',
                       'caption', 'input_message_content', 'description'):
        assert hasattr(obj, known_attr)


def test_cached_sticker():
    data = {'sticker_file_id': 'def456'}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'sticker'
    obj = InlineQueryResultCachedSticker('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultCachedSticker abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'sticker_file_id',
                       'input_message_content'):
        assert hasattr(obj, known_attr)


def test_cached_video():
    data = {'video_file_id': 'def456', 'title': 'My video',
            'caption': 'Pls loop'}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'video'
    obj = InlineQueryResultCachedVideo('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultCachedVideo abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'video_file_id', 'title',
                       'caption', 'input_message_content', 'description'):
        assert hasattr(obj, known_attr)


def test_cached_voice():
    data = {'voice_file_id': 'def456', 'title': 'My voice',
            'caption': 'Pls loop'}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'voice'
    obj = InlineQueryResultCachedVoice('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultCachedVoice abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'voice_file_id', 'title',
                       'caption', 'input_message_content'):
        assert hasattr(obj, known_attr)


def test_contact():
    data = {'phone_number': '+15555555555', 'first_name': 'Jack'}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'contact'
    obj = InlineQueryResultContact('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultContact abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'phone_number',
                       'first_name', 'last_name', 'thumb_url', 'thumb_width',
                       'thumb_height', 'input_message_content'):
        assert hasattr(obj, known_attr)


def test_document():
    data = {'title': 'Cool Document', 'document_url':
        'http://site.com/doc.pdf', 'mime_type': 'application/pdf'}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'document'
    obj = InlineQueryResultDocument('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultDocument abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'title',
                       'document_url', 'caption', 'description',
                       'thumb_url', 'thumb_width',
                       'thumb_height', 'input_message_content'):
        assert hasattr(obj, known_attr)


def test_game():
    data = {'game_short_name': 'fun'}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'game'
    obj = InlineQueryResultGame('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultGame abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'game_short_name'):
        assert hasattr(obj, known_attr)


def test_gif():
    data = {'gif_url': 'http://site.com/img.gif',
            'thumb_url': 'http://site.com/img.png'}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'gif'
    obj = InlineQueryResultGif('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultGif abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'gif_url',
                       'gif_duration', 'caption', 'title',
                       'thumb_url', 'gif_width',
                       'gif_height', 'input_message_content'):
        assert hasattr(obj, known_attr)


def test_location():
    data = {'latitude': 37.872059, 'longitude': -122.257812,
            'title': 'On top of the world'}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'location'
    obj = InlineQueryResultLocation('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultLocation abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'latitude',
                       'longitude', 'live_period', 'title',
                       'thumb_url', 'thumb_width',
                       'thumb_height', 'input_message_content'):
        assert hasattr(obj, known_attr)


def test_mpeg4_gif():
    data = {'mpeg4_url': 'http://site.com/img.gif',
            'thumb_url': 'http://site.com/img.png'}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'mpeg4_gif'
    obj = InlineQueryResultMpeg4Gif('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultMpeg4Gif abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'mpeg4_url',
                       'mpeg4_duration', 'caption', 'title',
                       'thumb_url', 'mpeg4_width',
                       'mpeg4_height', 'input_message_content'):
        assert hasattr(obj, known_attr)


def test_photo():
    data = {'photo_url': 'http://site.com/img.jpg',
            'thumb_url': 'http://site.com/img.png'}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'photo'
    obj = InlineQueryResultPhoto('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultPhoto abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'photo_url',
                       'caption', 'title', 'description',
                       'thumb_url', 'photo_width',
                       'photo_height', 'input_message_content'):
        assert hasattr(obj, known_attr)


def test_venue():
    data = {'latitude': 37.872059, 'longitude': -122.257812,
            'title': 'Campanile', 'address': 'Sather Tower, Berkeley, CA 94720'}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'venue'
    obj = InlineQueryResultVenue('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultVenue abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'latitude',
                       'longitude', 'title', 'address', 'foursquare_id',
                       'thumb_url', 'thumb_width',
                       'thumb_height', 'input_message_content'):
        assert hasattr(obj, known_attr)


def test_video():
    data = {'video_url': 'https://my.site/vid.mp4', 'mime_type': 'video/mp4',
            'thumb_url': 'https://my.site/thumb.png', 'title': 'The best video'}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'video'
    obj = InlineQueryResultVideo('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultVideo abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'input_message_content',
                       'video_url', 'mime_type', 'thumb_url', 'video_width',
                       'video_height', 'video_duration', 'description',
                       'title', 'caption'):
        assert hasattr(obj, known_attr)


def test_voice():
    data = {'voice_url': 'https://my.site/voice.ogg', 'title': 'The best voice'}
    expected = data.copy()
    expected['id'] = 'abc123'
    expected['type'] = 'voice'
    obj = InlineQueryResultVoice('abc123', **data)
    assert expected == obj.to_dict()
    assert '<InlineQueryResultVoice abc123>' == repr(obj)

    for known_attr in ('id', 'type', 'reply_markup', 'input_message_content',
                       'voice_url', 'voice_duration', 'title', 'caption'):
        assert hasattr(obj, known_attr)
