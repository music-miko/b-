from pyrogram.types import CallbackQuery
from bot.utils.buttons import main_menu

def register(app):
    @app.on_callback_query()
    async def handle_support(client, query: CallbackQuery):
        if query.data == "support":
            await query.message.edit_text("💬 Contact @YourSupportUsername", reply_markup=main_menu())