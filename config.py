import os


def _required_env(name):
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(
            f"Missing required environment variable {name}. "
            "Set it in your deployment environment before starting the bot."
        )
    return value


def _required_int_env(name):
    value = _required_env(name)
    try:
        return int(value)
    except ValueError as exc:
        raise RuntimeError(
            f"Environment variable {name} must be a valid integer."
        ) from exc


# Telegram application credentials and identifiers.
API_ID = _required_int_env("API_ID")
API_HASH = _required_env("API_HASH")
BOT_TOKEN = _required_env("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME", "").strip()
BOT_TEXT = ":𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®:"
OWNER_ID = _required_int_env("OWNER_ID")
CHANNEL_ID = _required_int_env("CHANNEL_ID")
CHANNEL_ID2 = _required_int_env("CHANNEL_ID2")
MONGO_URL = _required_env("MONGO_URL")
PREMIUM_LOGS = _required_int_env("PREMIUM_LOGS")

join = '<a href="">✳️ JOIN BACKUP</a>'
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY", "").strip()
UNSPLASH_QUERY = os.getenv("UNSPLASH_QUERY", "animal baby").strip()
ADMIN_BOT_USERNAME = os.getenv("ADMIN_BOT_USERNAME", "").strip().lstrip("@")
THUMB_URL = os.getenv(
    "THUMB_URL",
    "https://i.ibb.co/DPCmWSKV/1000003297-3.png",
).strip()
