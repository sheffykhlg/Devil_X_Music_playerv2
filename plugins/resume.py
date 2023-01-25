# Powered By @Teams_devil @misterjack18
# ©️ Copy Right By Teams_devil Or misterjack18 
# Any Problem To Report @Team_devil or @sabyahaapnehai
# Bot Owner @Teams_devil Or @misterjack18

from pyrogram import filters
from pyrogram.types import Message

from Devil.config import BANNED_USERS
from Devil.strings import get_command
from Devil import app
from Devil.core.call import Devill
from Devil.utils.database import is_music_playing, music_on
from Devil.utils.decorators import AdminRightsCheck

# Commands
RESUME_COMMAND = get_command("RESUME_COMMAND")


@app.on_message(
    filters.command(RESUME_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await Anon.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention)
    )
