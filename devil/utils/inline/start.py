# Powered By @Teams_devil @misterjack18

from typing import Union
from pyrogram.types import InlineKeyboardButton

from Devil.config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from Devil import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="?? ???????????????? ?",
                url=f"https://t.me/{app.username}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="?? ??????????????",
                url=f"https://t.me/sabyahaapnehai",
            ),
            InlineKeyboardButton(
                text="?????????????? ??",
                url=f"https://t.me/Teams_devil",
            )
        ],
        [
            InlineKeyboardButton(
                text="? ?????? ?????????????? ?", callback_data="settings_helper"
            )
        ]
    ]
    
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="? ??????? ???? ???????? ?????????? ? ?",
                url=f"https://t.me/{app.username}?startgroup=true"),
        ],
        [
            InlineKeyboardButton(
                text="?? ??????????????",
                url=f"https://t.me/sabyahaapnehai"),
            InlineKeyboardButton(
                text="?????????????? ??",
                url=f"https://t.me/Teams_devil")
        ],
        [
            InlineKeyboardButton(
                text="? ? ???????????????? ? ?",
                callback_data="settings_back_helper"
            )
        ]
    ]
            
    return buttons
