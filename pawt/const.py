BASE_PATH = "https://api.telegram.org/bot{token}/"

API_PATH = {
    "get_updates": "getUpdates",
    "get_me": "getMe",
    "send_message": "sendMessage",
    "forward_message": "forwardMessage",
    "send_photo": "sendPhoto",
    "send_audio": "sendAudio",
    "send_document": "sendDocument",
    "send_video": "sendVideo",
    "send_voice": "sendVoice",
    "send_video_note": "sendVideoNote",
    "send_media_group": "sendMediaGroup",
    "send_location": "sendLocation",
    "edit_message_live_location": "editMessageLiveLocation",
    "stop_message_live_location": "stopMessageLiveLocation",
    "send_venue": "sendVenue",
    "send_contact": "sendContact",
    "send_chat_action": "sendChatAction",
    "get_user_profile_photos": "getUserProfilePhotos",
    "get_file": "getFile",
    "kick_chat_member": "kickChatMember",
    "unban_chat_member": "unbanChatMember",
    "restrict_chat_member": "restrictChatMember",
    "promote_chat_member": "promoteChatMember",
    "export_chat_invite_link": "exportChatInviteLink",
    "set_chat_photo": "setChatPhoto",
    "delete_chat_photo": "deleteChatPhoto",
    "set_chat_title": "setChatTitle",
    "set_chat_description": "setChatDescription",
    "pin_chat_message": "pinChatMessage",
    "unpin_chat_message": "unpinChatMessage",
    "leave_chat": "leaveChat",
    "get_chat": "getChat",
    "get_chat_administrators": "getChatAdministrators",
    "get_chat_members_count": "getChatMembersCount",
    "get_chat_member": "getChatMember",
    "set_chat_sticker_set": "setChatStickerSet",
    "delete_chat_sticker_set": "deleteChatStickerSet",
    "answer_callback_query": "answerCallbackQuery",
    "edit_message_text": "editMessageText",
    "edit_message_caption": "editMessageCaption",
    "edit_message_reply_markup": "editMessageReplyMarkup",
    "delete_message": "deleteMessage",
    "send_sticker": "sendSticker",
    "get_sticker_set": "getStickerSet",
    "upload_sticker_file": "uploadStickerFile",
    "create_new_sticker_set": "createNewStickerSet",
    "add_sticker_to_set": "addStickerToSet",
    "set_sticker_position_in_set": "setStickerPositionInSet",
    "delete_sticker_from_set": "deleteStickerFromSet",
    "answer_inline_query": "answerInlineQuery",
    "send_invoice": "sendInvoice",
    "answer_shipping_query": "answerShippingQuery",
    "answer_pre_checkout_query": "answerPreCheckoutQuery",
    "send_game": "sendGame",
    "set_game_score": "setGameScore",
    "get_game_high_scores": "getGameHighScores",
}

MAX_LENGTH = {"text": 4096, "caption": 200}
