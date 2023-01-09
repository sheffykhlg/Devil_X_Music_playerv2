# Powered By @Teams_devil @misterjack18
# ©? Copy Right By Teams_devil Or misterjack18 
# Any Problem To Report @sabyahaapnehai or @Teams_devil
# Bot Owner @Teams_devil Or @misterjack18

from pyrogram import filters
from pyrogram.types import Message

from Devil import config
from Devil.strings import get_command
from Devil import app
from Devil.misc import SUDOERS
from Devil.utils.database import add_off, add_on
from Devil.utils.decorators.language import language

# Commands
VIDEOMODE_COMMAND = get_command("VIDEOMODE_COMMAND")


@app.on_message(filters.command(VIDEOMODE_COMMAND) & SUDOERS)
@language
async def videoloaymode(client, message: Message, _):
    usage = _["vidmode_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "download":
        await add_on(config.YTDOWNLOADER)
        await message.reply_text(_["vidmode_2"])
    elif state == "m3u8":
        await add_off(config.YTDOWNLOADER)
        await message.reply_text(_["vidmode_3"])
    else:
        await message.reply_text(usage)
