# Powered By @Teams_devil @misterjack18
# ©️ Copy Right By Teams_devil Or misterjack18 
# Any Problem To Report @Teams_devil or @sabyahaapnehai
# Bot Owner @Teams_devil Or @misterjack18

import asyncio
from datetime import datetime

from Devil import config
from Devil import app
from Devil.core.call import Devill, autoend
from Devil.utils.database import (get_client, is_active_chat,
                                       is_autoend)


async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        while not await asyncio.sleep(
            config.AUTO_LEAVE_ASSISTANT_TIME
        ):
            from DevilX.core.userbot import assistants

            for num in assistants:
                client = await get_client(num)
                try:
                    async for i in client.iter_dialogs():
                        chat_type = i.chat.type
                        if chat_type in [
                            "supergroup",
                            "group",
                            "channel",
                        ]:
                            chat_id = i.chat.id
                            if (
                                chat_id != Devil.config.LOG_GROUP_ID
                                and chat_id != -1001599873829
                            ):
                                if not await is_active_chat(chat_id):
                                    try:
                                        await client.leave_chat(
                                            chat_id
                                        )
                                    except:
                                        continue
                except:
                    pass


asyncio.create_task(auto_leave())


async def auto_end():
    while not await asyncio.sleep(5):
        if not await is_autoend():
            continue
        for chat_id in autoend:
            timer = autoend.get(chat_id)
            if not timer:
                continue
            if datetime.now() > timer:
                if not await is_active_chat(chat_id):
                    autoend[chat_id] = {}
                    continue
                autoend[chat_id] = {}
                try:
                    await Devill.stop_stream(chat_id)
                except:
                    continue
                try:
                    await app.send_message(
                        chat_id,
                        "🌷 𝐃𝐯𝐥 𝐁𝐨𝐭 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐀𝐮𝐭𝐨  𝐋𝐞𝐟𝐭 𝐓𝐡𝐞 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 𝐁𝐞𝐚𝐜𝐚𝐮𝐬𝐞 𝐍𝐨 𝐎𝐧𝐞 𝐀𝐜𝐭𝐢𝐯𝐞 𝐎𝐧 𝐕𝐨𝐢𝐜𝐞 𝐜𝐡𝐚𝐭 🌷.",
                    )
                except:
                    continue


asyncio.create_task(auto_end())

