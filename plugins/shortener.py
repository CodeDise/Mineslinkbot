from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from database.database import db
from helper_func import admin, to_small_caps
from config import *
import asyncio

@Client.on_message(filters.command("shortener") & filters.private & admin)
async def shortener_panel(client, message):
    config = await db.get_shortener_config()

    url = config.get("url", "Not Set")
    api = config.get("api", "Not Set")
    time_sec = config.get("time", 0)

    time_str = f"{time_sec} seconds"
    if time_sec >= 3600:
        time_str = f"{time_sec // 3600} Hours"

    text = (
        f"<b>⚙️ {to_small_caps('Shortener Configuration')}</b>\n\n"
        f"<b>{to_small_caps('Current URL')}:</b> `{url}`\n"
        f"<b>{to_small_caps('Current API')}:</b> `{api}`\n"
        f"<b>{to_small_caps('Verification Time')}:</b> `{time_str}`\n\n"
        f"{to_small_caps('Select a setting to change')}:"
    )

    buttons = [
        [
            InlineKeyboardButton(to_small_caps("Set URL"), callback_data="set_short_url"),
            InlineKeyboardButton(to_small_caps("Set API"), callback_data="set_short_api")
        ],
        [
            InlineKeyboardButton(to_small_caps("Set Time"), callback_data="set_short_time")
        ],
        [
            InlineKeyboardButton(to_small_caps("Close"), callback_data="close_shortener")
        ]
    ]

    await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons))
