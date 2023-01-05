# Powered By @TeamDevil
 @misterjack18

from typing import Union, List
from pyrogram import filters
from Devil.config import COMMAND_PREFIXES

## Team Devil 

def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)

