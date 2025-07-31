from pyrogram.types import CallbackQuery
from bot.database import stock
from bot.utils.buttons import main_menu

def register(app):
    @app.on_callback_query()
    async def handle_stock(client, query: CallbackQuery):
        if query.data == "stock":
            items = stock.get_all_items()
            text = "📦 Stock:\n" + "\n".join([f"- {i['name']}: {i['quantity']}" for i in items])
            await query.message.edit_text(text, reply_markup=main_menu())