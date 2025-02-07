from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "3500"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = "https://t.me/zlz1zl"
SUPPORT_CHANNEL = "https://t.me/zlz1zl"

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))


FAILED = "https://graph.org/file/8882cbd7cc786826d9ecb.jpg"
