import telebot
from telebot import types

global actors
actors = dict()


bot = telebot.TeleBot('6512133921:AAFMaVgr14Qe8-YN6Bc9VXrIRKbcyYW2upM')

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
    x = (actors[call.message.chat.id][1])
    y = (actors[call.message.chat.id][2])
    z = (actors[call.message.chat.id][3])
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
        etap1= open('text/1etap.txt', 'rb')
        bot.send_message(call.message.chat.id, etap1)
        img1 = open('img/etap1.png', 'rb')
        bot.send_photo(call.message.chat.id, img1, reply_markup=markup )

    if call.data == "v1":
        y += 1
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Далее', callback_data="game2")
        markup.add(btn1)
        answer1 = open('text/answer1.txt', 'rb')
        bot.send_message(call.message.chat.id, answer1)
        bot.send_message(call.message.chat.id, f"Деньги: {x}, Энергия: {y}, Баллы: {z}", reply_markup=markup)

    if call.data == "v2":
        y -= 1
        z += 10
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Далее', callback_data="game2")
        markup.add(btn1)
        answer2 = open('text/answer2.txt', 'rb')
        bot.send_message(call.message.chat.id, answer2)
        bot.send_message(call.message.chat.id, f"<b>Деньги:</b> <em>{x}</em>, Энергия: {y}, Баллы: {z}",parse_mode='html', reply_markup=markup)

    if call.data == "game2":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='1. Занять у родителей и купить домашку', callback_data="v3")
        btn2 = types.InlineKeyboardButton(text='2. Прийти без домашки ', callback_data="v4")
        markup.add(btn1, btn2)
        bot.send_message(call.message.chat.id, f'Ты забыл вовремя сделать домашку по дискретной математике, а сдавать её уже завтра. У тебя есть знакомые, которые могут помочь за символическую плату, но до стипендии ещё неделя и придётся занять деньги у родителей. Либо пойти на пару без домашки.')
        file2 = open('img/etap2.png', 'rb')
        bot.send_photo(call.message.chat.id, file2, reply_markup=markup)

    if call.data == "v3":
        x -= 500
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Далее', callback_data="game3")
        markup.add(btn1)
        answer3 = open('text/answer3.txt', 'rb')
        bot.send_message(call.message.chat.id, answer3)
        bot.send_message(call.message.chat.id, f"Деньги: {x}, Энергия: {y}, Баллы: {z}", reply_markup=markup)

    if call.data == "v4":
        y -= 1
        z += 15
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Далее', callback_data="game3")
        markup.add(btn1)
        answer4 = open('text/answer4.txt', 'rb')
        bot.send_message(call.message.chat.id, answer4)
        bot.send_message(call.message.chat.id, f"Деньги: {x}, Энергия: {y}, Баллы: {z}", reply_markup=markup)

bot.polling(non_stop=True, interval= 0)