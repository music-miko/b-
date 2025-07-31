from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🎁 Buy", callback_data="buy"),
         InlineKeyboardButton("👤 Profile", callback_data="profile")],
        [InlineKeyboardButton("💰 Deposit", callback_data="deposit"),
         InlineKeyboardButton("💬 Support", callback_data="support")],
        [InlineKeyboardButton("❓ FAQ", callback_data="faq"),
         InlineKeyboardButton("📦 Stock", callback_data="stock")]
    ])