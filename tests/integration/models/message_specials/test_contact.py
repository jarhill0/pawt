from ... import bm, tg, user

chat = tg.chat(user)


def test_send_contact():
    with bm.use_cassette('test_contact__test_send'):
        contact = chat.send_contact(phone_number='+15555555555',
                                    first_name='John').contact
        assert contact == contact.send(user).contact
