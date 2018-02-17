from ..base import PAWTBase


class ChatMember(PAWTBase):
    KNOWN_ATTRS = ('status', 'until_date', 'can_be_edited',
                   'can_change_info', 'can_post_messages',
                   'can_edit_messages', 'can_delete_messages',
                   'can_invite_users', 'can_restrict_members',
                   'can_pin_messages', 'can_promote_members',
                   'can_send_messages', 'can_send_media_messages',
                   'can_send_other_messages', 'can_add_web_page_previews')

    def __init__(self, tg, data):
        super().__init__(tg)

        user_data = data['user']
        self.user = self._tg.user(data=user_data)
        del data['user']

        for attr_name in ChatMember.KNOWN_ATTRS:
            setattr(self, attr_name, data.get(attr_name))

    def __repr__(self):
        return '<ChatMember {}>'.format(self.user.id)
