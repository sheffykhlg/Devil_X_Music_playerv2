import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "17323890"))
    API_HASH = os.environ.get("API_HASH", "6bd39253d6505762ec92cee9bbeec8bb")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5983809475:AAEkhDHjL2HDnTH0CDycSZiq2jlfpBS7_mY")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQAvi3OVLRdWN3mcuhgygP5KdpO_UpCXuYsfoJPZCyuvqvZZtlHYaW0OPWAy5L4ofEMi9aedyzqhtDqMa_fWxeqbLTRWrKHcdhFlrjOHTpMDoVFMsAY3lpj6ikSAkGdj6IqeDdEc7ko_aorT3Pnro5wxXpK8bzqpE2P1IuEacX7xdrNfebZwfLumMuBodtDJREtW_LHEkBw02-WYJXcSIGjv0k8ctiIzw_JvIZOUFI4VTf-jrpJ0dSpOPfrqxXgneMXg7fTBebTbbe6vlbIbKRH4TKudbQCpijWDOGBONZabKzmbSVg_2Uu12Xoi0_6AbZ7ncEbbw8Qs3JyYsKy58owuAAAAAUA84eUA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Devil_x_music_bot")
    SUPPORT = os.environ.get("SUPPORT", "https://t.me/sabyahaapnehai") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/Teams_devil") # Your Channel
    Source_code = os.environ.get("Source_code"," abe laude  repo chahiye to group join kar 🤨🤨") #your Source_code
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/490d4f6fa16e4bdff4c0c.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5372699109")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
