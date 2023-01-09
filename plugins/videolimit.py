# Powered By @Teams_devil @misterjack18
# ©? Copy Right By Teams_devil Or misterjack18 
# Any Problem To Report @Teams_devil or @sabyahaapnehai
# Bot Owner @Teams_devil Or @misterjack18

from pyrogram import filters
from pyrogram.types import Message

from Devil.strings import get_command
from Devil import app
from Devil.misc import SUDOERS
from Devil.utils.database import set_video_limit
from Devil.utils.decorators.language import language

VIDEOLIMIT_COMMAND = get_command("VIDEOLIMIT_COMMAND")


@app.on_message(filters.command(VIDEOLIMIT_COMMAND) & SUDOERS)
@language
async def set_video_limit_kid(client, message: Message, _):
    if len(message.command) != 2:
        usage = _["vid_1"]
        return await message.reply_text(usage)
    message.chat.id
    state = message.text.split(None, 1)[1].strip()
    if state.lower() == "disable":
        limit = 0
        await set_video_limit(limit)
        return await message.reply_text(_["vid_4"])
    if state.isnumeric():
        limit = int(state)
        await set_video_limit(limit)
        if limit == 0:
            return await message.reply_text(_["vid_4"])
        await message.reply_text(_["vid_3"].format(limit))
    else:
        return await message.reply_text(_["vid_2"])
