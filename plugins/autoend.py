 # Powered By @Teams_devil @misterjack18
# ©️ Copy Right By Teams_devil Or misterjack18 
# Any Problem To Report @Teams_devil or @sabyahaapnehai
# Bot Owner @Teams_devil Or @misterjack18 IF You Fresh Any Problem To Contact The DevilXmusicbot Owner

from pyrogram import filters

from Devil import config
from Devil.strings import get_command
from Devil import app
from Devil.misc import SUDOERS
from Devil.utils.database import autoend_off, autoend_on
from Devil.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "🔰 𝐔𝐬𝐚𝐠𝐞 🔰 :\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "🔰 𝐀𝐮𝐭𝐨 𝐄𝐧𝐝 𝐒𝐭𝐫𝐞𝐚𝐦 𝐄𝐧𝐚𝐛𝐥𝐞𝐝 ✅.\n\n💥 𝐃𝐯𝐥 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐖𝐢𝐥𝐥 𝐀𝐮𝐭𝐨 𝐋𝐞𝐚𝐯𝐞 𝐓𝐡𝐞 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 𝐖𝐡𝐞𝐧 𝐀𝐧𝐲𝐨𝐧𝐞 𝐍𝐨 𝐀𝐯𝐭𝐢𝐯𝐞 𝐓𝐡𝐞 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 𝐀𝐧𝐝 𝐁𝐨𝐭 𝐒𝐞𝐧𝐝 𝐀 𝐋𝐞𝐚𝐯𝐞 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 📝."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("🔰 𝐀𝐮𝐭𝐨 𝐄𝐧𝐝 𝐒𝐭𝐫𝐞𝐚𝐦 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝 ❎.")
    else:
        await message.reply_text(usage)

