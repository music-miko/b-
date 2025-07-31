from pyrogram.types import CallbackQuery
from bot.utils.buttons import main_menu

def register(app):
    @app.on_callback_query()
    async def handle_faq(client, query: CallbackQuery):
        if query.data == "faq":
            await query.message.edit_text(
                "❓ FAQ:\n1. How to buy?\n2. How to deposit?\n3. What if stock is out?",
                reply_markup=main_menu()
            )