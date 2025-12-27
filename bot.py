from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8077015457:AAFyjdn9IkFmU8IVFwhFTc0GWY22l4QkIK0"

# состояния
WAITING = "WAITING"
HAS_NAME = "HAS_NAME"
HAS_SURNAME = "HAS_SURNAME"

states = {}
data = {}

back_keyboard = ReplyKeyboardMarkup(
    [["Назад"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    states[user_id] = WAITING
    data[user_id] = {}

    await update.message.reply_text(
        "Введите имя:",
        reply_markup=back_keyboard
    )

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    states.pop(user_id, None)
    data.pop(user_id, None)

    await update.message.reply_text(
        "Бот выключен. Для начала введите /start",
        reply_markup=ReplyKeyboardRemove()
    )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    state = states.get(user_id, WAITING)

    if text == "Назад":
        if state == HAS_NAME:
            states[user_id] = WAITING
            await update.message.reply_text("Введите имя:", reply_markup=back_keyboard)
        elif state == HAS_SURNAME:
            states[user_id] = HAS_NAME
            await update.message.reply_text(
                "Введите фамилию:",
                reply_markup=back_keyboard
            )
        else:
            await update.message.reply_text("Вы уже в начале.")
        return

    if state == WAITING:
        data[user_id]["name"] = text
        states[user_id] = HAS_NAME
        await update.message.reply_text(
            "Введите фамилию:",
            reply_markup=back_keyboard
        )

    elif state == HAS_NAME:
        data[user_id]["surname"] = text
        states[user_id] = HAS_SURNAME

        name = data[user_id]["name"]
        surname = data[user_id]["surname"]

        await update.message.reply_text(
            f"Вас зовут {name} {surname}",
            reply_markup=ReplyKeyboardRemove()
        )

        await update.message.reply_text("Введите имя:", reply_markup=back_keyboard)

        states[user_id] = WAITING
        data[user_id] = {}

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("stop", stop))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

app.run_polling()
