from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from bot.database import stock, users
from bot.utils.buttons import main_menu

def register(app):
    @app.on_callback_query()
    async def handle_buy(client, query: CallbackQuery):
        data = query.data
        if data == "buy":
            items = stock.get_all_items()
            buttons = [[InlineKeyboardButton(item["name"], callback_data=f"buy_{item['name']}")] for item in items]
            buttons.append([InlineKeyboardButton("❌ Cancel", callback_data="cancel")])
            await query.message.edit_text("Select a product to buy:", reply_markup=InlineKeyboardMarkup(buttons))
        elif data.startswith("buy_"):
            name = data.split("_", 1)[1]
            item = stock.get_item(name)
            user = users.get_user(query.from_user.id)
            if item and item["quantity"] > 0:
                if user["balance"] >= item.get("price", 0):
                    stock.decrement_item(name)
                    users.add_order(query.from_user.id, name)
                    users.decrease_balance(query.from_user.id, item.get("price", 0))
                    await query.message.edit_text(f"✅ You bought {name}", reply_markup=main_menu())
                else:
                    await query.message.edit_text("❌ Not enough balance.", reply_markup=main_menu())
            else:
                await query.message.edit_text("❌ Out of stock.", reply_markup=main_menu())