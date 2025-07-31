from pyrogram.types import CallbackQuery
from bot.database import users
from bot.utils.buttons import main_menu

def register(app):
    @app.on_callback_query()
    async def handle_profile(client, query: CallbackQuery):
        if query.data == "profile":
            user = users.get_user(query.from_user.id)
            text = f"👤 Profile\nBalance: ${user['balance']}\nTotal Orders: {len(user['orders'])}"
            await query.message.edit_text(text, reply_markup=main_menu())