import telebot

bot = telebot.TeleBot('6009563530:AAE_7locOzitACeHL1RzvalMGQ8-Es97RKo')
@bot.message_handler(commands = ['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)