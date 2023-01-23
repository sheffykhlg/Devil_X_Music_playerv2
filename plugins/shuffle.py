# Powered By @Teams_devil @misterjack18
# ©? Copy Right By Teams_devil Or misterjack18 
# Any Problem To Report @Teams_devil or @sabyahaapnehai
# Bot Owner @Teams_devil Or @misterjack18

import random

from pyrogram import filters
from pyrogram.types import Message

from Devil.config import BANNED_USERS
from Devil.strings import get_command
from Devil import app
from Devil.misc import db
from Devil.utils.decorators import AdminRightsCheck

# Commands
SHUFFLE_COMMAND = get_command("SHUFFLE_COMMAND")


@app.on_message(
    filters.command(SHUFFLE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def admins(Client, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    check = db.get(chat_id)
    if not check:
        return await message.reply_text(_["admin_21"])
    try:
        popped = check.pop(0)
    except:
        return await message.reply_text(_["admin_22"])
    check = db.get(chat_id)
    if not check:
        check.insert(0, popped)
        return await message.reply_text(_["admin_22"])
    random.shuffle(check)
    check.insert(0, popped)
    await message.reply_text(
        _["admin_23"].format(message.from_user.first_name)
    )
