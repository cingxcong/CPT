import asyncio
import importlib

from pyrogram import idle
from Extractor.modules import ALL_MODULES


async def sumit_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Extractor.modules." + all_module)

    print("» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")
    # Pyrogram's idle() manages the process signal handlers and exits on
    # SIGINT/SIGTERM. Avoid replacing those handlers with asyncio.Event.set,
    # which is synchronous and cannot be passed to loop.create_task().
    await idle()
    print("» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")


def main():
    try:
        asyncio.run(sumit_boot())
    except KeyboardInterrupt:
        print("Interrupted by user.")
    finally:
        print("Bot stopped.")


if __name__ == "__main__":
    main()
