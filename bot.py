import telebot
import skysmart
from colorama import init, Fore
bot = telebot.TeleBot('5292921227:AAFkkN6-GnIDW55FMlQhgiFt8gsdq3eHvzQ')
bot.delete_webhook()
taskHash = ""
results = []
@bot.message_handler(commands=['start'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Вставь ссылку на задание SkySmart :)")
        bot.register_next_step_handler(message, get_room)  # следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /start')

def get_room(message):
    global taskHash
    temp = message.text.split('/')
    for i in range(len(temp)):
        if len(temp[i]) == 10:
            taskHash = temp[i]
    bot.send_message(message.from_user.id, 'Ищем ответы...')
    get_answers(message)
    print_answ(message)

def get_answers(message):
    global taskHash
    global results
    results = skysmart.answerparse(taskHash)
    bot.send_message(message.from_user.id, 'Ответы найдены!')
    bot.register_next_step_handler(message, print_answ)


def print_answ(message):
    i = 0
    res = ''
    for item in results:
        if 'Вопрос' in item:
            i = i + 1
            res += str(i) + str(item) + '\n'
        else:
            res += str(item) + '\n'
    bot.send_message(message.from_user.id,res)


bot.polling(none_stop=True, interval=0)
