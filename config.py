import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAamn_ZIspB71qStlj7w-UUHmCKGoPcLHOVH7wTbMfdU0K6dSYrpatG0xfvRTNgcxUecrhQ5hf0ux91R_0GpSVUn0D_3s1BfG1IviNahyLSPSPXF2oH2YzhOAx6uuIhTgzulcXJaIsbSGjyKQUM3VkaGhvIKOi77xc0tC01ra-q1Ziky5xLiEwEXJ59A4QUySKsZ45fP8-5FQdSudydosMn39KPd5q6rYeiOZSbEslAsSsNXsD0ZdehwEIHKqvlSdkDB4wWp61Sl1b69UpUthAJlFMvzX0nUr5dVZL7hTaZOznz0Ga-ksqdL5jpAczp4hnyKY0TM4-JGLDxVi_t9dX-f6VfmgA")
BOT_TOKEN = getenv("BOT_TOKEN" , "5571871730:AAE8Bw-9kSqvFBNqtQ8PXuZWCkdbiNpvzFU")
BOT_NAME = getenv("BOT_NAME", "DRAGO MUSIC BOT")
API_ID = int(getenv("API_ID", "13526566"))
API_HASH = getenv("API_HASH", "6db5a4cd6cf59ac58da1d78c6653f0aa")
OWNER_NAME = getenv("OWNER_NAME", "GOD_DRAGOOP")
ALIVE_NAME = getenv("ALIVE_NAME", "GOD DRAGOOP")
BOT_USERNAME = getenv("BOT_USERNAME", "DRAGO_MUSIC_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "𝗗𝗥𝗔𝗚𝗢 𝗠𝗨𝗦𝗜𝗖 𝗔𝗦𝗦𝗜𝗦𝗧")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "DRAGO_CHEATS_CHAT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DRAGO_CHEATS")
SUDO_USERS = list(map(int, getenv("SUDO_USERS" , "1543260546").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/logi-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
