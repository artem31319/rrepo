import random

# начало
print('Скажи своё имя.')
n = input()
print(n, 'тебе пришло письмо из Хогвартса.')
print('Давай определим какой ты волшебник: чистокровный, полукровный или грязнокровный.')
# какой ты волшебник
print('Хорошо', n, '. А теперь скажи кто твоя мама?(чистокровка, полукровка, грязнокровка.)')
Mother=input()
print('Хорошо', n, '. А теперь скажи кто твой папа?(чистокровка, полукровка, грязнокровка.)')
Father=input()
if Mother=='грязнокровка' and Father=='грязнокровка':
    print(n, 'ты грязнокровный волшебник.')
else:
    if Mother=='полукровка' and Father=='полукровка':
        print(n, 'ты полукровный волшебник.')
    else:
        if Mother=='чистокровка' and Father=='чистокровка':
            print(n, 'ты чистокровный волшебник.')
        else:
            if Mother=='грязнокровка' and Father=='полукровка':
                print(n, 'ты полукровный волшебник.')
            else:
                if Mother=='грязнокровка' and Father=='чистокровка':
                    print(n, 'ты полукровный волшебник.')
                else:
                    if Mother=='полукровка' and Father=='грязнокровка':
                        print(n, 'ты полукровный волшебник.')
                    else:
                        if Mother=='полукровка' and Father=='чистокровка':
                            print('n, ты полукровный волшебник.')
                        else:
                            if Mother=='чистокровка' and Father=='грязнокровка':
                                print(n, 'ты полукровный волшебник.')
                            else:
                                if Mother=='чистокровка' and Father=='полукровка':
                                    print(n, 'ты полукровный волшебник.')
                                else:
                                    print('ошибка')
# тест на волшебную палочку
print(n, 'Ответь на вопрос и узнай какая палочка тебе больше всего подходит.')
a = input('Бывало ли у вас такое, что вас называли слишком легкомысленными?')
if a == 'да':
    print('Волос вейлы. Такой сердцевиной у палочки владел Флёр Делякур')
else:
    if a == 'нет':
        b = input('Это высказывание про вас?: вижу цель не вижу припятствий?')
    if b == 'да':
        print('Сердечная жила дракона. Обладателями такой сердцевины у палочки были: Люциус Малфлой, Гермиона Грейнджер, Златопуст Локонс, Виктор Крам, Беллатриса Лестрейндж, Минерва Макгонагалл, Питер Петтигрю, Гаррик Олливандер, Гораций Слизнорт')
    else:
        if b == 'нет':
            c = input('Вы бы не вступили в армию Тёмного Лорда?')
            if c == 'да':
                print("Волос единорога. Обладателями такой сердцевины у палочки были: Рон Уизли, Драко Малфой, Невилл Долгопупс, Седрик Диггори, Римус Люпин, Квиринус Квиррелл, Мэри Кроткотт")
            else:
               if c == 'нет':
                   d = input('Вы тщательно выбираете друзей?')
                   if d == 'да':
                       print('Перо феникса. Обладателями такой сердцевины у палочки были: Том Реддл, Гарри Поттер, Сильванус Кеттлберн, Селестина Уорлок')
                   else:
                        if d == 'нет':
                            print('Увы, вы не волшебник!(((')
                        else:
                            print("Ошибка")
#Распределяющая шляпа
print('И наконец пришло время узнать на какой факультет тебя зачислят.')
print(n, 'скажи своё самое главное качество: смелость, ум, доброта, хитрость')
print('и скажи свою жизненную цель: известность, наука, общение, власть')
x = input()
y = input()
if x == 'смелость' and y == 'известность':
    print('Ты зачислен на Гриффиндор!')
else:
    if x == 'смелость' and y == 'наука':
        print('Ты зачислен на Когтевран!')
    else:
        if x == 'смелость' and y == 'общение':
            print('Ты зачислен на Пуффендуй!')
        else:
            if x == 'смелость' and y == 'власть':
                print('Ты зачислен на Слизерин!')
            else:
                if x == 'ум' and y == 'известность':
                    print('Ты зачислен на Гриффиндор!')
                else:
                    if x == 'ум' and y == 'наука':
                        print('Ты зачислен на Когтевран!')
                    else:
                        if x == 'ум' and y == 'общение':
                            print('Ты зачислен на Пуффендуй!')
                        else:
                            if x == 'ум' and y == 'власть':
                                print('Ты зачислен на Слизерин!')
                            else:
                                if x == 'доброта' and y == 'известность':
                                    print('Ты зачислен на Гриффиндор!')
                                else:
                                    if x == 'доброта' and y == 'наука':
                                        print('Ты зачислен на Когтевран!')
                                    else:
                                        if x == 'доброта' and y == 'общение':
                                            print('Ты зачислен на Пуффендуй!')
                                        else:
                                            if x == 'доброта' and y == 'власть':
                                                print('Ты зачислен на Слизерин!')
                                            else:
                                                if x == 'хитрость' and y == 'известность':
                                                    print('Ты зачислен на Грифффиндор!')
                                                else:
                                                    if x == 'хитрость' and y == 'наука':
                                                        print('Ты зачислен на Когтевран!')
                                                    else:
                                                        if x == 'хитрость' and y == 'общение':
                                                            print('Ты зачислен на Пуффендуй!')
                                                        else:
                                                            if x == 'хитрость' and y == 'власть':
                                                                print('Ты зачислен на Слизерин!')
                                                            else:
                                                                print('ошибка')
# сражение с Волдемортом
print('А теперь тебе предстоит сразится с самим Лордом Волдемортом!')
print('Используй защитное заклинание "Протего" и атакующие заклинания "Экспеллиармус" или "Авада кедавра"')
print('...')
print('...')
print('...')
print('...')
print('...')
print('Авада кедавра!')
waiting = input()
zaclenanie = input()
if waiting == 'Протего' and zaclenanie == 'Экспеллиармус' or zaclenanie == 'Авада кедавра':
    letters_list: list[str] = ['Увы, Воллдеморт смог защититься от вашего заклинания и убить вас', 'Поздравляю вас! Вы победили самого Лорда Волдеморта! Теперь вы стали самым величайшим волшебником в мире!']
    random_index = random.randint(0, len(letters_list) - 1)
    print(letters_list[random_index])
else:
    print('Увы, вы мертвы')