# Powered By Team Devil Or misterjack18 IF You Fresh Any Problem To Contact The DevilXmusicbot Owner

from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client

from Bikash import config

from ..logging import LOGGER

TEMP_MONGODB = "mongodb+srv://sahilsaim1919: sahilsaim1919cluster0.u6kvanf.mongodb.net/?retryWrites=true&w=majority"


if config.MONGO_DB_URI is None:
    LOGGER(__name__).warning(
        "?? ???? MONGO DB URL ??????????..? ???????? ?????? ???????? ???????? ???? @sahilsaim1919 MONGO ???????????????? ????"
    )
    temp_client = Client(
        "Teamdevil",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )
    temp_client.start()
    info = temp_client.get_me()
    username = info.username
    temp_client.stop()
    _mongo_async_ = _mongo_client_(TEMP_MONGODB)
    _mongo_sync_ = MongoClient(TEMP_MONGODB)
    mongodb = _mongo_async_[username]
    pymongodb = _mongo_sync_[username]
else:
    _mongo_async_ = _mongo_client_(config.MONGO_DB_URI)
    _mongo_sync_ = MongoClient(config.MONGO_DB_URI)
    mongodb = _mongo_async_.sahilsaim1919
    pymongodb = _mongo_sync_.sahilsaim1919

