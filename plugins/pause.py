# Powered By @Teams_devil @misterjack18
# ©? Copy Right By Teams_devil Or misterjack18 
# Any Problem To Report @Teams_devil or @misterjack18
# Bot Owner @Teams_devil Or @sabyahaapnehai

from pyrogram import filters
from pyrogram.types import Message

from Devil.config import BANNED_USERS
from Devil.strings import get_command
from Devil import app
from Devil.core.call import Bikashh as Anon
from Devil.utils.database import is_music_playing, music_off
from Devil.utils.decorators import AdminRightsCheck

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@app.on_message(
    filters.command(PAUSE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await Anon.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention)
    )
