import random

cand = 0

# Логика бота: берем остаток от деления на 5 или 1
def bot_logic(num):
    if num % 5 == 0:
        return 1
    else:
        return num % 5


def init_candy(message):
    global cand
    # Общее кол-во конфет
    cand = random.randint(20, 30)
    # Кто первый
    bot_action = random.choice([True, False])
    mess = f'Конфет на столе {cand}\n'
    mess += 'Можно взять до 4шт\n'
    mess += 'Первый ход '
    if bot_action:
        mess += 'Бота\n'
        get_candies = bot_logic(cand)
        cand -= get_candies
        mess += f'Бот взял {get_candies}конфет\n'
        mess += f'Конфет на столе {cand}\n'
        mess += 'Можно взять до 4шт\n'
        mess += f'Ваш ход {message.from_user.first_name}'
    else:
        mess += str(message.from_user.first_name)
    return mess


def input_candies(message):
    global cand
    if message.text in '1234' and int(message.text) <= cand:
        get_candies = int(message.text)
        cand -= get_candies
        mess = f'{message.from_user.first_name} взял {get_candies} конфет\n'
        if cand <= 0:
            mess += f'{message.from_user.first_name}, Победа!'
            return mess
        else:
            get_candies = bot_logic(cand)
            cand -= get_candies
            mess += f'Бот взял {get_candies} конфет\n'
            if cand == 0:
                mess += 'Бот победил'
            else:
                mess += f'Конфет на столе {cand}\n'
                mess += 'Можно взять до '
                if cand >= 4:
                    mess += '4 шт\n'
                else:
                    mess += f'{cand}шт.'
            return mess
    else:
        return 'Неверный ввод'