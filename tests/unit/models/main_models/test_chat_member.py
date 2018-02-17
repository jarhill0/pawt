from pawt import Telegram
from pawt.models import ChatMember


def test_chat_member():
    tg = Telegram('')
    user = dict(id=12345, is_bot=False, first_name='Johnny')
    data = {'can_add_web_page_previews': True,
            'can_be_edited': False,
            'can_change_info': False,
            'can_delete_messages': False,
            'can_edit_messages': False,
            'can_invite_users': False,
            'can_pin_messages': True,
            'can_post_messages': True,
            'can_promote_members': True,
            'can_restrict_members': False,
            'can_send_media_messages': True,
            'can_send_messages': True,
            'can_send_other_messages': True,
            'status': 'kicked',
            'until_date': 1518830605,
            'user': user}

    memb = ChatMember(tg=tg, data=data)

    assert repr(memb) == '<ChatMember 12345>'

    for key, value in data.items():
        assert getattr(memb, key) == value
