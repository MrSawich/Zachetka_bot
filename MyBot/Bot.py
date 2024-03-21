import telebot
from telebot import types

global actors
actors = dict()
bot = telebot.TeleBot('6512133921:AAFMaVgr14Qe8-YN6Bc9VXrIRKbcyYW2upM')

def send_stats(call, markup):
    bot.send_message(call.message.chat.id,
                     f"<b>Деньги:</b> <em>{actors[call.message.chat.id][1]}</em>, <b>Энергия:</b> <em>{actors[call.message.chat.id][2]}</em>, <b>Баллы:</b> <em>{actors[call.message.chat.id][3]}</em>",
                     reply_markup=markup,
                     parse_mode='html')

@bot.message_handler(commands=['start'])
def main(message):
    global actors
    if message.chat.id not in actors:
        actors[message.chat.id] = [f"{message.from_user.first_name} {message.from_user.last_name}", 1000, 10, 0]
    print(actors)
    markup = types.InlineKeyboardMarkup()
    rule = types.InlineKeyboardButton(text='Правила игры', callback_data="rule")
    game = types.InlineKeyboardButton(text='Начать игру', callback_data="game")
    markup.add(rule, game)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup= markup)

@bot.callback_query_handler(func = lambda call: True)
def menu (call):
    if call.data == "rule":
        markup = types.InlineKeyboardMarkup()
        game = types.InlineKeyboardButton(text='Начать игру', callback_data="game")
        markup.add(game)
        bot.send_message(call.message.chat.id, f'<b><em>Суть игры</em></b> Зачётка - это ролевая игра про студента первого курса.\
        Он сталкивается с ситуациями по ходу обучения и получает баллы, чтобы получить зачеты по предметам. \
        Игроку даны базовые значения, такие как 1. Деньги, 2. Энергия 3. Баллы Ситуации, которые происходят по ходу игры, \
        требуют эти самые ресурсы. Если ресурсов не хватает, то и использовать этот вариант ответа нельзя.', parse_mode='html', reply_markup= markup)

    if call.data == "game":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='1. Пропустить пару', callback_data="v1")
        btn2 = types.InlineKeyboardButton(text='2. Ели как собраться и пойти', callback_data="v2")
        markup.add(btn1, btn2)
        etap = open('text/1etap.txt', 'rb')
        bot.send_message(call.message.chat.id, etap)
        img = open('img/etap1.png', 'rb')
        bot.send_photo(call.message.chat.id, img, reply_markup=markup )

    if call.data == "v1":
        actors[call.message.chat.id][2] += 1
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Далее', callback_data="game2")
        markup.add(btn1)
        answer = open('text/answer1.txt', 'rb')
        bot.send_message(call.message.chat.id, answer)
        send_stats(call, markup)

    if call.data == "v2":
        actors[call.message.chat.id][2] -= 1
        actors[call.message.chat.id][3] += 10
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Далее', callback_data="game2")
        markup.add(btn1)
        answer = open('text/answer2.txt', 'rb')
        bot.send_message(call.message.chat.id, answer)
        send_stats(call, markup)

    if call.data == "game2":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='1. Занять у родителей и купить домашку', callback_data="v3")
        btn2 = types.InlineKeyboardButton(text='2. Прийти без домашки ', callback_data="v4")
        markup.add(btn1, btn2)
        etap = open('text/2etap.txt', 'rb')
        bot.send_message(call.message.chat.id, etap)
        img = open('img/etap2.png', 'rb')
        bot.send_photo(call.message.chat.id, img, reply_markup=markup)

    if call.data == "v3":
        actors[call.message.chat.id][1] -= 500
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Далее', callback_data="game3")
        markup.add(btn1)
        answer = open('text/answer3.txt', 'rb')
        bot.send_message(call.message.chat.id, answer)
        send_stats(call, markup)

    if call.data == "v4":
        actors[call.message.chat.id][2] -= 1
        actors[call.message.chat.id][3] += 15
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Далее', callback_data="game3")
        markup.add(btn1)
        answer = open('text/answer4.txt', 'rb')
        bot.send_message(call.message.chat.id, answer)
        send_stats(call, markup)

    if call.data == "game3":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='1. Вычислить воришку необычным способом', callback_data="v5")
        btn2 = types.InlineKeyboardButton(text='2. Забить на ситуацию, в общаге все общее', callback_data="v6")
        markup.add(btn1, btn2)
        etap = open('text/3etap.txt', 'rb')
        bot.send_message(call.message.chat.id, etap)
        img = open('img/etap3.png', 'rb')
        bot.send_photo(call.message.chat.id, img, reply_markup=markup)

    if call.data == "v5":
        actors[call.message.chat.id][1] += 200
        actors[call.message.chat.id][2] -= 1
        actors[call.message.chat.id][3] += 10
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Далее', callback_data="game4")
        markup.add(btn1)
        answer = open('text/answer5.txt', 'rb')
        bot.send_message(call.message.chat.id, answer)
        send_stats(call, markup)

    if call.data == "v6":
        actors[call.message.chat.id][1] -= 300
        actors[call.message.chat.id][2] -= 1
        actors[call.message.chat.id][3] += 15
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Далее', callback_data="game4")
        markup.add(btn1)
        answer = open('text/answer6.txt', 'rb')
        bot.send_message(call.message.chat.id, answer)
        send_stats(call, markup)

    if call.data == "game4":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='1. Пересилить себя и пройти мимо', callback_data="v7")
        btn2 = types.InlineKeyboardButton(text='2. Закупиться булками и кофейком, но опоздать', callback_data="v8")
        markup.add(btn1, btn2)
        etap = open('text/4etap.txt', 'rb')
        bot.send_message(call.message.chat.id, etap)
        img = open('img/etap4.png', 'rb')
        bot.send_photo(call.message.chat.id, img, reply_markup=markup)

    if call.data == "v7":
        actors[call.message.chat.id][2] -= 1
        actors[call.message.chat.id][3] += 15
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Далее', callback_data="game5")
        markup.add(btn1)
        answer = open('text/answer7.txt', 'rb')
        bot.send_message(call.message.chat.id, answer)
        send_stats(call, markup)

    if call.data == "v8":
        actors[call.message.chat.id][1] -= 200
        actors[call.message.chat.id][2] += 1
        actors[call.message.chat.id][3] += 5
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Далее', callback_data="game5")
        markup.add(btn1)
        answer = open('text/answer8.txt', 'rb')
        bot.send_message(call.message.chat.id, answer)
        send_stats(call, markup)

    if call.data == "game5":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='1. Честно пробегать весь семестр', callback_data="v9")
        btn2 = types.InlineKeyboardButton(text='2. Подделать справки', callback_data="v10")
        markup.add(btn1, btn2)
        etap = open('text/5etap.txt', 'rb')
        bot.send_message(call.message.chat.id, etap)
        img = open('img/etap5.png', 'rb')
        bot.send_photo(call.message.chat.id, img, reply_markup=markup)

    if call.data == "v9":
        actors[call.message.chat.id][2] -= 2
        actors[call.message.chat.id][3] += 30
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Далее', callback_data="final")
        markup.add(btn1)
        answer = open('text/answer9.txt', 'rb')
        bot.send_message(call.message.chat.id, answer)
        send_stats(call, markup)

    if call.data == "v10":
        actors[call.message.chat.id][1] -= 400
        actors[call.message.chat.id][2] += 1
        actors[call.message.chat.id][3] -= 20
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Далее', callback_data="final")
        markup.add(btn1)
        answer = open('text/answer10.txt', 'rb')
        bot.send_message(call.message.chat.id, answer)
        send_stats(call, markup)

    if call.data == "final":


    if call.data == "holidays":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Поработать на складе', callback_data="h1")
        btn2 = types.InlineKeyboardButton(text='Тусить с друзьями', callback_data="h2")
        btn3 = types.InlineKeyboardButton(text='Далее', callback_data="game6")
        markup.add(btn1, btn2, btn3)
        etap = open('text/holidays.txt', 'rb')
        bot.send_message(call.message.chat.id, etap, reply_markup=markup)

    if call.data == "h1":

    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

# git status
# git add .
# git commit -m "№ комит"
# git push

bot.polling(non_stop=True, interval= 0)
