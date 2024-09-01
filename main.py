import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
from config import TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# key - list UID, data - list with products
shopping_lists = {
    "testlist": ["сгущенка", "вафли", "майонез", "курочка 500 гр"]
}        

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Here are the available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/source - Get a link to the source code"
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome! Please set your shopping list ID using the command /set <list ID>. Anyone who has this list ID have access to the list, so it's essentially a password, not name. Use up to 64 alpha-numerical chars. Thank you!")

async def list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check that user has shopping_list_id configured, if yes - list all products
    selected_list = context.user_data.get('shopping_list_id')
    if selected_list:
        list_contens = shopping_lists.get(selected_list)
        if not list_contens:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your selected list ID: {selected_list}\nBlank list")
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your selected list ID: {selected_list}\n{"\n".join(list_contens)}")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="You don't have any list selected. Please set your shopping list ID using the command /set <list ID>. Anyone who has this list ID have access to the list, so it's essentially a password, not name. Use up to 64 alpha-numerical chars.")

async def set_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    def is_valid_list_id(s: str) -> bool:
        return s.isalnum() and len(s) <= 64
    if context.args:
        shopping_list_id = context.args[0]
        if is_valid_list_id(shopping_list_id):
            context.user_data['shopping_list_id'] = shopping_list_id
            await update.message.reply_text(f"Shopping list ID set to: {shopping_list_id}")
        else:
            await update.message.reply_text(f"List ID is not valid, please check that ot fits requirements.")
    else:
        await update.message.reply_text("Please provide a shopping list ID after /set.")

async def source(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Source code: https://github.com/AndreyNaydenov/lista_za_kupovinu_bot"
    )

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    help_handler = CommandHandler('help', help_command)
    start_handler = CommandHandler('start', start)
    source_handler = CommandHandler('source', source)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    list_handler = CommandHandler('list', list_command)
    set_handler = CommandHandler('set', set_command)
    application.add_handler(help_handler)
    application.add_handler(start_handler)
    application.add_handler(source_handler)
    application.add_handler(set_handler)
    application.add_handler(list_handler)
    application.add_handler(unknown_handler)
    
    application.run_polling()
