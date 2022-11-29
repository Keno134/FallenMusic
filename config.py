from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "12410871"))
API_HASH = getenv("API_HASH", "f7a7de22f129870e74bd87e9ef5320bd")
BOT_TOKEN = getenv("BOT_TOKEN", "5418087889:AAFwuUGyhN0jOQPkLKYo308AjgrB80WTmOY")
BOT_NAME = getenv("BOT_NAME","Cʜɪғᴜʏᴜ 𝑿 Mᴜsɪᴄ")
BOT_USERNAME = getenv("BOT_USERNAME", "Chifuyu_X_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "BerlinXbaap")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Mysticbots_Support")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/f6107be777a5125f07539.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/184accb94eee032152a03.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQBVJ8cvnSJCQNwzXjB_781qRGA-8FwfnnlTlwn54ds8kYdgfjA3kGpUBLOHlTIPq7p3nlZYSSZFFPyJrdB74r7wCHxYiYhi6-L2PdyRjfg8C2dfbqZSq6DwjdN1l5x9XEumKBkZH5nzUKrhJ3cQ3gOaor65VeLDFZ6_FMSzjL8C_bhrx70cPsY4S-czWlZl-Mt-JNzKyi-_0dxQwqyDmKxCRKh63YL6F7wxvxfrZ6oFBhxaZKbjw-4sDYXgYa9e6R-JY_lqdAFEaujlsF5LPa-Eww711DCkV9oRD1cSEDm66fEfNpyorWgoPDlOw9P33Nce3xq2UeNZmdYr_fgNZ56DAAAAAVRpAwcA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5732788031").split()))
