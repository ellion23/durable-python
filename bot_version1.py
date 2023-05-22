import config
import telebot

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=["text"])
def text(message):
    print(message)
    if message.text == "вау":
        bot.send_message(message.chat.id, "yeah, "+ message.from_user.first_name + "<3")
    if (message.text == "yes") or (message.text == "да") or (message.text == "Yes"):
        bot.send_message(message.chat.id, "mrrrrr")
    if (message.text == "no") or (message.text == "нет") or (message.text == "No"):
        bot.send_message(message.chat.id, "^｡‸｡^")
    else:
        bot.send_message(message.chat.id, "you're cool, wanna prrr, " + message.from_user.first_name + " ? " + "say: yes or no")

# heh
bot.infinity_polling()
