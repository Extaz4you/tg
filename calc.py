def calc(message):
    args = message.text.split()
    if len(args) > 1:
        arg = ''.join(args[1:])
        try:
            result = eval(arg)
            return str(result)
        except:
            return 'Некорректно заданное выражение'
    else:
        return 'Введите выражение в виде: /calc "выражение"'