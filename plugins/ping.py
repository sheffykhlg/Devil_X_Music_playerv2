# Powered By @Teams_devil @misterjack18
# ©? Copy Right By Teams_devil Or misterjack18 
# Any Problem To Report Teams_devil or @sabyahaapnehai
# Bot Owner @Teams_devil Or @misterjack18

from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from Devil.config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from Devil.strings import get_command
from Devil import app
from Devil.core.call import Devill
from Devil.utils import bot_sys_stats
from Devil.utils.decorators.language import language

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    filters.command(PING_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await Bikashh.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        )
    )
