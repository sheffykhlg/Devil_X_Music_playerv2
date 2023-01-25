# Powered By @Teams_devil @misterjack18
# ©️ Copy Right By Teams_devil Or misterjack18 
# Any Problem To Report @Teams_devil or @sabyahaapnehai
# Bot Owner @Teams_devil Or @misterjack18

import asyncio

from pyrogram import filters
from pyrogram.types import CallbackQuery, Message

from Devil.config import BANNED_USERS, MUSIC_BOT_NAME, adminlist, lyrical
from Devil.strings import get_command
from Devil import app
from Devil.core.call import Bikashh
from Devil.misc import db
from Devil.utils.database import get_authuser_names, get_cmode
from Devil.utils.decorators import (ActualAdminCB, AdminActual,
                                         language)
from Devil.utils.formatters import alpha_to_int

### Multi-Lang Commands
RELOAD_COMMAND = get_command("RELOAD_COMMAND")
RESTART_COMMAND = get_command("RESTART_COMMAND")


@app.on_message(
    filters.command(RELOAD_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def reload_admin_cache(client, message: Message, _):
    try:
        chat_id = message.chat.id
        admins = await app.get_chat_members(
            chat_id, filter="administrators"
        )
        authusers = await get_authuser_names(chat_id)
        adminlist[chat_id] = []
        for user in admins:
            if user.can_manage_voice_chats:
                adminlist[chat_id].append(user.user.id)
        for user in authusers:
            user_id = await alpha_to_int(user)
            adminlist[chat_id].append(user_id)
        await message.reply_text(_["admin_20"])
    except:
        await message.reply_text(
            "🌷𝐀𝐝𝐦𝐢𝐧 𝐋𝐢𝐬𝐭 𝐑𝐞𝐟𝐫𝐞𝐬𝐡 𝐅𝐚𝐢𝐥𝐞𝐝 ❌, 𝐌𝐚𝐤𝐞 𝐒𝐮𝐫𝐞 𝐘𝐨𝐮 𝐏𝐫𝐨𝐦𝐨𝐭𝐞𝐝 𝐓𝐡𝐞 𝐃𝐞𝐯𝐢𝐥 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐲 ✅."
        )


@app.on_message(
    filters.command(RESTART_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminActual
async def restartbot(client, message: Message, _):
    mystic = await message.reply_text(
        f"🌷 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 𝐅𝐞𝐰 𝐌𝐢𝐧𝐮𝐭𝐞𝐬 ,{MUSIC_BOT_NAME} 𝐈𝐬 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐈𝐧 𝐓𝐡𝐢𝐬 𝐂𝐡𝐚𝐭 ♻️."
    )
    await asyncio.sleep(1)
    try:
        db[message.chat.id] = []
        await Devill.stop_stream(message.chat.id)
    except:
        pass
    chat_id = await get_cmode(message.chat.id)
    if chat_id:
        try:
            await app.get_chat(chat_id)
        except:
            pass
        try:
            db[chat_id] = []
            await Devill.stop_stream(chat_id)
        except:
            pass
    return await mystic.edit_text(
        f"🌷𝐃𝐞𝐯𝐢𝐥 𝐁𝐨𝐭 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐞𝐝 ✅ {MUSIC_BOT_NAME} 𝐈𝐬 𝐘𝐨𝐮𝐫 𝐂𝐡𝐚𝐭, 🌸 𝐍𝐨𝐰 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐁𝐨𝐭 𝐀𝐠𝐚𝐢𝐧 & 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 𝐀𝐠𝐚𝐢𝐧 ✅..."
    )


@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return


@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return


@app.on_callback_query(
    filters.regex("stop_downloading") & ~BANNED_USERS
)
@ActualAdminCB
async def stop_download(client, CallbackQuery: CallbackQuery, _):
    message_id = CallbackQuery.message.message_id
    task = lyrical.get(message_id)
    if not task:
        return await CallbackQuery.answer(
            "🌷 𝐃𝐨𝐰𝐧𝐋𝐨𝐚𝐝 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐃𝐨𝐧𝐞 ✅.", show_alert=True
        )
    if task.done() or task.cancelled():
        return await CallbackQuery.answer(
            "🌷 𝐃𝐨𝐰𝐧𝐋𝐨𝐚𝐝 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐃𝐨𝐧𝐞 ✅  & 𝐂𝐚𝐧𝐜𝐞𝐥 ❌.",
            show_alert=True,
        )
    if not task.done():
        try:
            task.cancel()
            try:
                lyrical.pop(message_id)
            except:
                pass
            await CallbackQuery.answer(
                "🔰 𝐃𝐨𝐰𝐧𝐋𝐨𝐚𝐝 𝐂𝐥𝐨𝐬𝐞 ❌.", show_alert=True
            )
            return await CallbackQuery.edit_message_text(
                f"📌 𝐃𝐨𝐰𝐧𝐋𝐨𝐚𝐝𝐢𝐧𝐠 𝐂𝐥𝐨𝐬𝐞𝐝 𝐁𝐲 {CallbackQuery.from_user.mention} ❌"
            )
        except:
            return await CallbackQuery.answer(
                "🌷 𝐃𝐨𝐰𝐧𝐋𝐨𝐚𝐝 𝐂𝐥𝐨𝐬𝐞 𝐅𝐚𝐢𝐥𝐞𝐝 ❌ 𝐂𝐥𝐨𝐬𝐞 𝐃𝐨𝐰𝐧𝐋𝐨𝐚𝐝𝐢𝐧𝐠...", show_alert=True
            )
    await CallbackQuery.answer(
        "🌷 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐑𝐞𝐜𝐨𝐠𝐧𝐢𝐳𝐞 𝐓𝐡𝐞 𝐎𝐧𝐠𝐨𝐢𝐧𝐠 𝐓𝐚𝐬𝐤 📌.", show_alert=True
    )
