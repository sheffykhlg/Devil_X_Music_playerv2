# 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 𝐚𝐧𝐝 𝐄𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭𝐬
import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

# 𝐈𝐧𝐭𝐞𝐫𝐧𝐚𝐥 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 (@𝐓𝐄𝐀𝐌𝐃𝐄𝐕𝐈𝐋)
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

# 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 //𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 @𝐓𝐄𝐀𝐌𝐃𝐄𝐕𝐈𝐋 
API_HASH = getenv("API_HASH", "XXXXX")
API_ID = int(getenv("API_ID", "XXXXX"))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "XXXXX")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "XXXXX")
BOT_IMAGE = getenv("BOT_IMAGE", "https://te.legra.ph/file/99d0261f0aa5512ad6753.jpg")
BOT_NAME = getenv("BOT_NAME", "XXXXX")
BOT_TOKEN = getenv("BOT_TOKEN", "12345:XXXXX")
BOT_USERNAME = getenv("BOT_USERNAME", "XXXXX")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
OWNER_NAME = getenv("OWNER_NAME", "😈😈𖣔ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋ🇲​.𝐑 𝐃𝐄𝐕𝐈𝐋")
OWNER_USERNAME = getenv("OWNER_USERNAME", "misterjack18")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/sahilsaim1919/Devil_X_Music_player") 
PING_IMAGE = gentenv("PING_IMAGE",  "https://te.legra.ph/file/b8e9c122763158456a2e8.jpg")
STRING_SESSION = getenv("STRING_SESSION", "session")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5372699109").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/sabyahaapnehai")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/Teams_devil")

# 𝐃𝐨 𝐍𝐨𝐭 𝐂𝐡𝐚𝐧𝐠𝐞 𝐓𝐡𝐢𝐬 𝐋𝐢𝐧𝐞𝐬 // 𝐈𝐠𝐧𝐨𝐫𝐞 𝐓𝐡𝐢𝐬 (😈😈𖣔ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋ🇲​.𝐑 𝐃𝐄𝐕𝐈𝐋) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
GIF_CHANNEL = getenv("GIF_CHANNEL", "https://t.me/CUTE_GIFS_All")
