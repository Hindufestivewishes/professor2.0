import re, time
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]: return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]: return False
    else: return default


# PyroClient Setup 
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
WEBHOOK = bool(environ.get("WEBHOOK", True)) # for web support on/off
PICS = (environ.get('PICS', 'https://graph.org/file/76836e6ea78206a62879e.jpg https://graph.org/file/13f659ac180bb9aca16bb.jpg https://graph.org/file/8ef64627a58819a5bff3e.jpg https://graph.org/file/c20b64a9f95d26817e483.jpg https://graph.org/file/bd7fb0fafd946f10a8a46.jpg https://graph.org/file/e9d81ff276a5926db647b.jpg https://graph.org/file/0f14b6707a9c89687760f.jpg https://graph.org/file/19aec0224e020e87157b1.jpg https://graph.org/file/5523b7993c346588f8f47.jpg https://graph.org/file/0e128d474b6d542f72791.jpg https://graph.org/file/ae47b160e1ec72ec5a90f.jpg https://graph.org/file/f1ae0d6a34df3868a0fd3.jpg')).split()
UPTIME = time.time()

# Admins, Channels & Users
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP', '-1002096640256')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
SECONDDB_URI = environ.get('SECONDDB_URI', "mongodb+srv://dqthedonar74:dqthedonar74@cluster0.hyysf85.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://devurl:devurl@cluster0.aekafsv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
FILE_DB_URL = environ.get("FILE_DB_URL", DATABASE_URL)
FILE_DB_NAME = environ.get("FILE_DB_NAME", DATABASE_NAME)
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Filters Configuration 
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', script.START_TXT)
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", script.BUTTON_LOCK_TEXT)
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', script.FORCE_SUB_TEXT)

WELCOM_PIC = environ.get("WELCOM_PIC", "https://te.legra.ph/file/3ad5a10fc20c028e40e20.png")
WELCOM_TEXT = environ.get("WELCOM_TEXT", script.WELCOM_TEXT)
PMFILTER = is_enabled(environ.get('PMFILTER', "True"), True)
G_FILTER = is_enabled(environ.get("G_FILTER", "True"), True)
BUTTON_LOCK = is_enabled(environ.get("BUTTON_LOCK", "True"), True)
RemoveBG_API = environ.get("RemoveBG_API", "")

# url shortner
SHORT_URL = environ.get("SHORT_URL")
SHORT_API = environ.get("SHORT_API")

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'devmovies2')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "False"), True)
PM_IMDB = is_enabled(environ.get('PM_IMDB', "False"), False)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "{file_name}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('LOG_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)
LOG_MSG = "{} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ....✨\n\n🗓️ Dᴀᴛᴇ : {}\n⏰ Tɪᴍᴇ : {}\n\n@dev_autof_bot"






