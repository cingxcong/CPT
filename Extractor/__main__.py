import asyncio
import importlib

from pyrogram import idle
from Extractor.modules import ALL_MODULES


async def sumit_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Extractor.modules." + all_module)

    print("» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")
    # Pyrogram idle() installs and handles the process signal handlers.
    await idle()
    print("» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")


def main():
    # Extractor.app is initialized during package import and uses this event
    # loop. Reuse it instead of asyncio.run(), which would create a second loop.
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(sumit_boot())
    except KeyboardInterrupt:
        print("Interrupted by user.")
    finally:
        pending = asyncio.all_tasks(loop)
        for task in pending:
            task.cancel()
        if pending:
            loop.run_until_complete(
                asyncio.gather(*pending, return_exceptions=True)
            )
        loop.close()
        print("Bot stopped.")


if __name__ == "__main__":
    main()
