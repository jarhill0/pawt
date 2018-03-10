from pawt.exceptions import APIException, BadArgument
from pawt.models import make_labeled_price
from pawt.models.reply_markup import force_reply
from .. import bm, game, tg, user

chat = tg.chat(user)


def test_load():
    with bm.use_cassette('test_chat__test_load'):
        chat.get_chat()
    assert chat.type.value == 'private'


def test_send_message():
    with bm.use_cassette('test_chat__test_send_message'):
        mess = chat.send_message('Hello world')
    assert mess.text == 'Hello world'


def test_special_arguments():
    with bm.use_cassette('test_chat__test_special_arguments'):
        messages = [
            chat.send_message('This is *bold*.', parse_mode='Markdown'),
            chat.send_message('https://github.com',
                              disable_web_page_preview=True),
            chat.send_message('Shh', disable_notification=True),
            chat.send_message('Talk to me', reply_markup=force_reply())
        ]

    assert messages[0].text == 'This is bold.'


def get_pdf():
    import os
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, 'denevi.pdf')


def test_send_document():
    with open(get_pdf(), 'rb') as pdf:
        with bm.use_cassette('test_chat__test_send_document'):
            mess = chat.send_document(pdf, 'Two short stories')

    assert mess.caption == 'Two short stories'


def test_send_video():
    with bm.use_cassette('test_chat__test_send_video'):
        mess = chat.send_video('https://i.imgur.com/LdE8jcw.mp4',
                               duration=8, width=100, height=400,
                               caption='baloncesto')
    assert mess.caption == 'baloncesto'


def test_send_voice():
    with bm.use_cassette('test_chat__test_send_voice'):
        mess = chat.send_voice(
            'https://upload.wikimedia.org/wikipedia/commons/4/47/Beethoven_Moonlight_2nd_movement.ogg',
            duration=125, caption='File:Beethoven Moonlight 2nd movement.ogg')
    assert mess.caption == 'File:Beethoven Moonlight 2nd movement.ogg'


def test_send_game():
    with bm.use_cassette('test_chat__test_send_game'):
        mess = chat.send_game(game)
    assert repr(mess.game).startswith('<Game ')


def test_send_photo():
    with bm.use_cassette('test_chat__test_send_photo'):
        mess = chat.send_photo(
            'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/C-17_test_sortie.jpg/800px-C-17_test_sortie.jpg',
            caption='From Wikimedia commons!')
    assert mess.caption == 'From Wikimedia commons!'


def test_send_contact():
    class Contact:
        pass

    contact = Contact()
    contact.phone_number = '+15555555555'
    contact.first_name = 'Johnny'
    contact.last_name = 'Appleseed'
    with bm.use_cassette('test_chat__test_send_contact'):
        chat.send_contact(contact)

    try:
        chat.send_contact(contact, '+15555555555')
        assert False, 'should raise BadArgument'
    except BadArgument:
        pass


def test_send_venue():
    class Venue:
        pass

    venue = Venue()
    venue.location = Venue()  # location, but whatever...
    venue.location.latitude = 37.8720789
    venue.location.longitude = -122.258008
    venue.title = 'The Campanile'
    venue.address = 'Sather Tower, Berkeley, CA 94720'
    venue.foursquare_id = None

    with bm.use_cassette('test_chat__test_send_venue'):
        chat.send_venue(venue)

    try:
        chat.send_venue(venue, 37.8720789)
        assert False, 'should raise BadArgument'
    except BadArgument:
        pass


def test_send_audio():
    with bm.use_cassette('test_chat__test_send_audio'):
        mess = chat.send_audio(
            'http://www.billwurtz.com/la-de-da-de-da-de-da-de-day-oh.mp3',
            caption='La-de-da-de-da-de-da-de-day-oh!', duration=191,
            performer='Bill Wurtz', title='La de da de da de da de day oh')
    assert mess.audio.duration == 191


def test_send_location():
    class Location:
        pass

    location = Location()
    location.latitude = 37.8720789
    location.longitude = -122.258008

    with bm.use_cassette('test_chat__test_send_location'):
        mess = chat.send_location(location, live_period=70)
    assert round(mess.location.latitude, 3) == round(37.8720789, 3)

    try:
        chat.send_location(location, latitude=78)
        assert False, 'should raise BadArgument'
    except BadArgument:
        pass


def get_mp4():
    import os
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, 'video_note.mp4')


def test_send_video_note():
    with open(get_mp4(), 'rb') as vid:
        with bm.use_cassette('test_chat__test_send_video_note'):
            mess = chat.send_video_note(vid, length=400, duration=15)


def test_send_bad_chat_action():
    try:
        chat.send_chat_action('Destroying humanity')
        assert False, 'should raise BadArgument'
    except BadArgument:
        pass


def test_send_invoice():
    with bm.use_cassette('test_chat__test_send_invoice'):
        try:
            chat.send_invoice(title='Widget', description='It is great',
                              payload='abc123',
                              provider_token='123456789qwertyuiop',
                              start_parameter='def456', currency='USD',
                              prices=[make_labeled_price('Cheap', 100)],
                              provider_data="{'price':0}",
                              photo_url='https://i.imgur.com/8ABRUYt.png',
                              photo_size=14, photo_width=597, photo_height=300,
                              need_name=False, need_phone_number=True,
                              need_email=False, need_shipping_address=True,
                              send_phone_number_to_provider=False,
                              send_email_to_provider=True, is_flexible=False)
        except APIException as e:
            # probably not connected
            assert 'PAYMENT_PROVIDER_INVALID' in str(e)


def test_forward_message():
    with bm.use_cassette('test_chat__test_forward_message'):
        message = chat.send_message('Yo yo yo!')
        new_message = message.forward(chat)
    assert new_message.id != message.id

