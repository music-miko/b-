from pyrogram.types import CallbackQuery
from bot.utils.buttons import main_menu
from config import ADMIN_ID

def register(app):
    @app.on_callback_query()
    async def handle_deposit(client, query: CallbackQuery):
        if query.data == "deposit":
            await query.message.edit_text(
                "💰 Send payment with your Telegram ID in the note. Then wait for admin approval.",
                reply_markup=main_menu()
            )
            await app.send_message(
                ADMIN_ID,
                f"📥 Top-up request from {query.from_user.mention} ({query.from_user.id}). Please verify and approve."
            )