import time

from pawt.exceptions import APIException, BadArgument
from pawt.models import make_labeled_price
from pawt.models.reply_markup import force_reply
from ... import bm, game, supergroup, tg, user

chat = tg.chat(user)


def test_load():
    with bm.use_cassette("test_chat__test_load"):
        chat.get_chat()
    assert chat.type.value == "private"


def test_send_message():
    with bm.use_cassette("test_chat__test_send_message"):
        mess = chat.send_message("Hello world")
    assert mess.text == "Hello world"


def test_special_arguments():
    with bm.use_cassette("test_chat__test_special_arguments"):
        messages = [
            chat.send_message("This is *bold*.", parse_mode="Markdown"),
            chat.send_message("https://github.com", disable_web_page_preview=True),
            chat.send_message("Shh", disable_notification=True),
            chat.send_message("Talk to me", reply_markup=force_reply()),
        ]

    assert messages[0].text == "This is bold."


def get_pdf():
    import os

    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, "denevi.pdf")


def test_send_document():
    with open(get_pdf(), "rb") as pdf:
        with bm.use_cassette("test_chat__test_send_document"):
            mess = chat.send_document(pdf, "Two short stories")

    assert mess.caption == "Two short stories"


def test_send_video():
    with bm.use_cassette("test_chat__test_send_video"):
        mess = chat.send_video(
            "https://i.imgur.com/LdE8jcw.mp4",
            duration=8,
            width=100,
            height=400,
            caption="baloncesto",
        )
    assert mess.caption == "baloncesto"


def test_send_voice():
    with bm.use_cassette("test_chat__test_send_voice"):
        mess = chat.send_voice(
            "https://upload.wikimedia.org/wikipedia/commons/4/47/Beethoven_Moonlight_2nd_movement.ogg",
            duration=125,
            caption="File:Beethoven Moonlight 2nd movement.ogg",
        )
    assert mess.caption == "File:Beethoven Moonlight 2nd movement.ogg"


def test_send_game():
    with bm.use_cassette("test_chat__test_send_game"):
        mess = chat.send_game(game)
    assert repr(mess.game).startswith("<Game ")


def test_send_photo():
    with bm.use_cassette("test_chat__test_send_photo"):
        mess = chat.send_photo(
            "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/C-17_test_sortie.jpg/800px-C-17_test_sortie.jpg",
            caption="From Wikimedia commons!",
        )
    assert mess.caption == "From Wikimedia commons!"


def test_send_contact():
    class Contact:
        pass

    contact = Contact()
    contact.phone_number = "+15555555555"
    contact.first_name = "Johnny"
    contact.last_name = "Appleseed"
    with bm.use_cassette("test_chat__test_send_contact"):
        chat.send_contact(contact)

    try:
        chat.send_contact(contact, "+15555555555")
        assert False, "should raise BadArgument"
    except BadArgument:
        pass


def test_send_venue():
    class Venue:
        pass

    venue = Venue()
    venue.location = Venue()  # location, but whatever...
    venue.location.latitude = 37.8720789
    venue.location.longitude = -122.258008
    venue.title = "The Campanile"
    venue.address = "Sather Tower, Berkeley, CA 94720"
    venue.foursquare_id = "abcdefg"

    with bm.use_cassette("test_chat__test_send_venue"):
        chat.send_venue(venue)

    try:
        chat.send_venue(venue, 37.8720789)
        assert False, "should raise BadArgument"
    except BadArgument:
        pass


def test_send_audio():
    with bm.use_cassette("test_chat__test_send_audio"):
        mess = chat.send_audio(
            "http://www.billwurtz.com/la-de-da-de-da-de-da-de-day-oh.mp3",
            caption="La-de-da-de-da-de-da-de-day-oh!",
            duration=191,
            performer="Bill Wurtz",
            title="La de da de da de da de day oh",
        )
    assert mess.audio.duration == 191


def test_send_location():
    class Location:
        pass

    location = Location()
    location.latitude = 37.8720789
    location.longitude = -122.258008

    with bm.use_cassette("test_chat__test_send_location"):
        mess = chat.send_location(location, live_period=70)
    assert round(mess.location.latitude, 3) == round(37.8720789, 3)

    try:
        chat.send_location(location, latitude=78)
        assert False, "should raise BadArgument"
    except BadArgument:
        pass


def get_mp4():
    import os

    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, "video_with_sound.mp4")


def test_send_video_note():
    with open(get_mp4(), "rb") as vid:
        with bm.use_cassette("test_chat__test_send_video_note"):
            mess = chat.send_video_note(vid, length=400, duration=15)


def test_send_bad_chat_action():
    try:
        chat.send_chat_action("Destroying humanity")
        assert False, "should raise BadArgument"
    except BadArgument:
        pass


def test_send_invoice():
    with bm.use_cassette("test_chat__test_send_invoice"):
        try:
            chat.send_invoice(
                title="Widget",
                description="It is great",
                payload="abc123",
                provider_token="123456789qwertyuiop",
                start_parameter="def456",
                currency="USD",
                prices=[make_labeled_price("Cheap", 100)],
                provider_data="{'price':0}",
                photo_url="https://i.imgur.com/8ABRUYt.png",
                photo_size=14,
                photo_width=597,
                photo_height=300,
                need_name=False,
                need_phone_number=True,
                need_email=False,
                need_shipping_address=True,
                send_phone_number_to_provider=False,
                send_email_to_provider=True,
                is_flexible=False,
            )
        except APIException as e:
            # probably not connected
            assert "PAYMENT_PROVIDER_INVALID" in str(e)


def test_forward_message():
    with bm.use_cassette("test_chat__test_forward_message"):
        message = chat.send_message("Yo yo yo!")
        chat.forward_message(chat, message.id)
        new_message = message.forward(chat)
    assert new_message.id != message.id


def get_png():
    import os

    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, "gradient2.png")


def test_supergroup():
    group = tg.chat(supergroup)
    with bm.use_cassette("test_chat__test_supergroup"):
        group.get_chat()
        if group.can_set_sticker_set:
            group.set_sticker_set("LazyPanda")
        link = group.export_invite_link()
        assert link
        for admin in group.get_administrators():
            assert admin.user.id
        message = group.send_message("gonna pin this")
        group.pin_message(message.id, disable_notification=True)
        group.unpin_message()
        group.pin_message(message, disable_notification=True)
        group.unpin_message()
        assert group.get_member_count()

        group.get_chat()
        if group.can_set_sticker_set:
            group.delete_sticker_set()
        group.set_title(group.title + "a")
        group.set_description((group.description or "") + "d")
        with open(get_png(), "rb") as pic:
            group.set_photo(pic)
        group.delete_photo()

        # getting a message from a user in this chat
        for item in tg.get_updates(timeout=0):
            if not item.message:
                continue
            if item.message.chat != supergroup:
                continue
            if not item.message.forward_from:
                continue
            if item.message.forward_from == user:
                continue
            author = item.message.forward_from

        assert author, "could not get user to test with"

        group.promote_member(author, can_change_info=True)
        group.restrict_member(
            author, can_add_web_page_previews=False, until_date=time.time() + 60
        )
        assert author == group.get_member(author).user
        group.kick_member(author, until_date=time.time() + 70)
        group.unban_member(author)

        group.leave()


def test_lazy():
    # test the PAWTLazy base class
    chat = tg.chat(user)
    with bm.use_cassette("test_chat__test_lazy"):
        try:
            chat.nonexistant_attr
            assert False, "AttributeError should be raised"
        except AttributeError:
            pass


def test_send_media_group():
    with bm.use_cassette("test_chat__test_send_media_group_1"):
        photo_obj = chat.send_photo(
            "https://upload.wikimedia.org/wikipedia/"
            "commons/thumb/d/df/Common_frog_rana_"
            "temporaria.jpg/800px-Common_frog_rana_"
            "temporaria.jpg"
        ).photo
        with open(get_mp4(), "rb") as vid:
            video_obj = chat.send_video(vid, caption="video caption").video

    media = [
        {
            "type": "photo",
            "media": "https://upload.wikimedia.org/wikipedia/"
            "commons/thumb/6/61/Frog_in_pond_0547.jpg"
            "/640px-Frog_in_pond_0547.jpg",
            "caption": "This is a frog",
        },
        photo_obj,
        video_obj,
        {
            "type": "photo",
            "media": "https://upload.wikimedia.org/wikipedia/"
            "commons/thumb/6/61/Frog_in_pond_0547.jpg"
            "/640px-Frog_in_pond_0547.jpg",
            "caption": "frog" * 76,
        },
        3,
    ]

    try:
        chat.send_media_group(media)
        assert False, "should raise BadArgument"
    except BadArgument as e:
        assert "type" in str(e)

    del media[-1]

    try:
        chat.send_media_group(media)
        assert False, "should raise BadArgument"
    except BadArgument as e:
        assert "long" in str(e).lower()

    del media[-1]

    with open(get_mp4(), "rb") as vid:
        local_vid = {
            "type": "video",
            "media": vid,
            "width": 400,
            "height": 300,
            "duration": 15,
        }
        media.append(local_vid)

        with bm.use_cassette("test_chat__test_send_media_group_2"):
            messages = chat.send_media_group(media)

    assert len(messages) == len(media)
