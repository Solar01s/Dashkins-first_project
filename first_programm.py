
# импортируем инструменты для кода----------------
import random # рандом
import datetime #дата время
import time # просто время
import winsound #звук
import tkinter as tk #для окон
# импортируем словари бот из другого файла
from DaSHkins_answers import *
# Вводное резюме-----------------
print('''
                                                                    DaSHkins: Привет, как дела?        
                                                                                                 
                                                            Напишите сообщение чтобы начать разговор 
''')
# словари пользователя-----------
greatingsP ={
"прив","здравств","xай",
"даров","салам","бонжур","банжур"
}
SadP ={
"груст",":(","обид","печал","грущ","бед","тильт", "фиг", "хер"
}
whatP={
"?","обЪяс","сколько","почему","зачем","где","что такое","кто такой"
    }
lichP={
"как дел","как настр","как у тебя дел","как твои дел","шо ты"
    }
fictionP={
"что ты уме","твои функци","что можешь","что ты можешь",
"что умеешь","что ты знаеш"
    }
pokaP={
"пока","до встр","до скор","досвида","покед","бай"
    }
today={
"сегодн","сейч","в данный моме","на сегодн","на данный моме"
    }
imbaP={
"крут","классн","весел","радост","идеал","прекрас","замечательно",
"великолепно","ура","рад","хорош","отличн","хороше","имб","хороши"
    }
blagoP={
"спасиб","от душ","спс","благодар","очень прият"
    }
soglP={
"поня","принял","понимаю","дошло","пон"
    }
nesoglP={
"не","ни в коем случа","ноу","не хочу"
    }
daP={
"ок","ладно","ага","да,","давай","угу","конечно","хочу","гоу",
"может быть","быть может","может","хочу","я готов","да"
    }
ktoP={
"кто ты","как тебя зовут","твое имя","какое у тябя имя","ты кто",
"для чего ты","что ты такое"
    }
podgP={
"выучить","подготовиться","завтра урок","скоро урок"
    }
delalP={
"чем занима","что дела","делал что","занимался чем","шо ты",
"ты чо","что ты дела"
    }
timeP= {
"утро","день","вечер","ноч","дня"
    }
neponP={
"не понял","не понятно","не понятно","не допер","не пон",
"не дошло","не прин","непонятно"
    }
all_day_greatings_P={
"доброго утр","доброе утр","утро добр","солнечного утр","утра доброго","проснулся",
"добрый ден","день добрый","дня доброго","середина дня","дня добренкого","добренький день",
"добрый вечер","вечер в хат","вечер добр","добренького вечера","доброго вечера","вечер добрый"
}
good_night ={
"доброй ночи","спокойной ночи","я спать","спок","споки ноки"
}
ogoP = {
"ого","ничего себе","вот это да","поражает","обалдеть","ниче се","нифига се","ошалеть","прикол"
    }
arifmetic_mathematicP={
"+","-","/","*",":"
    }
numbers_mathematicP ={
'0','1','2','3','4','5','6','7','8','9'
    }
good_words ={
"хорош","красив","полезн","пуш","прекрас","крут","невероят",
"умн","гени","клас","идеал",
"прикол","бомб","супер","сас","имб",
"кайф","прайм","луч","солн","интерес","класс",
"молодец","молодц","смешн","забавн"
    }
bad_words = {
"плох","ужас","дебил","идиот","идеот","итеот",
"итиот","даун","туп","ненорм","не норм","аутист",
"твар","балбес","болбес","говн",
"не полезн","неполезн","упыр","баран","козел",
"анскил","отшель","сук","суч","жопа",
"попа","жир","не красив","некрасив","паномар",
"писюн","фиг","хер","абобус","вонюч","глуп"
    }
you = {
"ты","вы"
    }
# Функционал (def)ы-----------------
def time_of_day():
    if any(time in user_message for time in all_day_greatings_P):
        hour = datetime.datetime.now().hour
        if 4<=hour<12:
            print(random.choice(utro_time_greatings_D))
            x = 1
            return x
        elif 12<=hour<18:
            print(random.choice(day_time_greatings_D))
            x = 1
            return x
        elif 17<=hour<23:
            print(random.choice(vecher_time_greatings_D))
            x = 1
            return x
        else:
            print(random.choice(night_time_greatings_D))
            x = 1
            return x
def DaSHkins_thinking():
    #звук отправки сообщения
    path = "C:/Users/рс/Downloads/free-sound-1674743345.wav"
    winsound.PlaySound(path,winsound.SND_FILENAME| winsound.SND_ASYNC)
    if len(user_message) > 50:
        print()
        print(random.choice(thinkingD), end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(1.0)
        print()
        print(random.choice(readyD))
        time.sleep(0.8)
    else:
        print()
        print(random.choice(thinkingD), end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print()
        print(random.choice(readyD))
        time.sleep(0.8)
def DaSHkins_greatings():
    if  any(greating  in user_message for greating in greatingsP):
        G = random.choice(greatings)
        global now_answer
        now_answer += G
        x = 1
        return x
    else:
        x = 0
        return x
def DaSHkins_sad():
    if  any(sad in user_message for sad in SadP):
        G = random.choice(sadD)
        global now_answer
        now_answer += G
        x = 1
        return x
    else:
        x = 0
        return x
def DaSHkins_lich():
    if  any(lich in user_message for lich in lichP):
        G = random.choice(lichD)
        global now_answer
        now_answer += G
        x = 1
        return x
    else:
        x = 0
        return x
def DaSHkins_poka():
    global now_answer
    if any(poka in user_message for poka in pokaP):
        G = random.choice(pokaD)
        now_answer += G
        x = 1
        return x
    if user_message.lower() in ["адьес","адиос","адеос","адьос","адьес,амигос"]:
        G = random.choice(amigosD)
        now_answer += G
        x = 1
        return x
    else:
        x = 0
        return x
def DaSHkins_imba():
    if any(im in user_message for im in imbaP):
        G = random.choice(imbaD)
        global now_answer
        now_answer += G
        x = 1
        return x
    else:
        x = 0
        return x
def DaSHkins_blagodarnost():
    if any(blago in user_message for blago in blagoP):
        G = random.choice(blagoD)
        global now_answer
        now_answer += G
        x = 1
        return x
    else:
        x = 0
        return x
def DaSHkins_neponyatno():
    if any(nepon in user_message for nepon in neponP):
        G = random.choice(neponD)
        global now_answer
        now_answer += G
        x = 1
        return x
    else:
        x = 0
        return x
def DaSHkins_ponyatno():
    if any(sogl in user_message for sogl in soglP):
        G = random.choice(soglD)
        global now_answer
        now_answer += G
        x = 1
        return x
    else:
        x = 0
        return x
def DaSHkins_nesoglasen():
    if any(nesogl in user_message for nesogl in nesoglP):
        G = random.choice(nesoglD)
        global now_answer
        now_answer += G
        x = 1
        return x
    else:
        x = 0
        return x
def DaSHkins_da():
    if any(da in user_message for da in daP):
        G = random.choice(daD)
        global now_answer
        now_answer += G
        x = 1
        return x
    else:
        x = 0
        return x
def DaSHkins_cho_delal():
    if any(delal in user_message for delal in delalP):
        G = random.choice(delalD)
        global now_answer
        now_answer += G
        x = 1
        return x
    else:
        x = 0
        return x
def DaSHkins_function():
    if any(fic in user_message for fic in fictionP):
        G = random.choice(functionD)
        global now_answer
        now_answer += G
        x = 1
        return x
    else:
        x = 0
        return x
def DaSHkins_kto_ti():
    if any(kto in user_message for kto in ktoP):
        G = random.choice(kto_tiD)
        global now_answer
        now_answer += G
        x = 1
        return x
    else:
        x = 0
        return x
def DaSHkins_OGO():
    if any(ogo in user_message for ogo in ogoP):
        G = random.choice(ogoD)
        global now_answer
        now_answer += G
        x = 1
        return x
    else:
        x = 0
        return x
def User_messages_lenght():
    lenght_user_message = len(user_message)
    G = "Количество символов в вашем сообщении:",lenght_pr
    global now_answer
    now_answer += G
#переменная с количеством сообщений пользователя
messages_quantity = 0

def user_messages_more():
    global now_answer
    messages_digital =[
    2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20
        ]
    digital_read = random.choice(messages_digital)
    if messages_quantity == digital_read:
        G = ""
        D = random.choice(more_messages)
        G += D
        G += str(digital_read)
        F = random.choice(more_messages2)
        G += F
        now_answer += G
        x = 1
        return x
    elif messages_quantity == 10:
        G = ""
        Y = random.choice(more_messages)
        G += Y
        G += "10"
        H = random.choice(more_messages2)
        G += H
        now_answer += G
        x = 1
        return x
    else:
        x = 0
        return x
def DaSHkins_math():
# условие работы функции

    if any(math in user_message for math in arifmetic_mathematicP) and any(mas in user_message for mas in numbers_mathematicP):
        print(random.choice(math_answerD))
        global now_answer
#для превращения в единый тип работы с выражениями
        words = user_message
        maths = ""
        for word in words:
            if word in ['1','2','3','4','5','6','7','8','9','0','+','-','*','/','.']:
                maths += word + " "
        try:
            print(maths, "=", eval(maths))
        except Exception as e:
            print(f"Извините, не удалось решить мат. пример:\n{maths}")
        '''
        symbs = list(words)
        all_symbs = []
        i = 0
        perfect_symbs = ['1','2','3','4','5','6','7','8','9','0','+','-','*','/','.']
        for i in range (len(symbs)):
            dig = symbs[i]
            if dig in perfect_symbs:
                all_symbs.append(dig)
            if dig == ',':
                all_symbs.append('.')
            if dig == ':':
                all_symbs.append('/')
            i = i + 1
        if all_symbs[0] == '*':
                all_symbs.pop(0)
        if all_symbs[0] == '/':
                all_symbs.pop(0)
        final = ' '.join(all_symbs)
#окончательное преобразование математического выражения
        now_number = "" # текущее число запоминания
        make_answer = [] # общий список
        for symbol in final:
            if symbol.isdigit() or symbol == '.':
                now_number += symbol
            else:
                if now_number:
                    make_answer.append(float(now_number))
                    now_number = ""
                if symbol in '+-*/':
                    make_answer.append(symbol)
        if now_number:
            make_answer.append(float(now_number))
# решение математического выражения

        resualt = make_answer[0]
        i = 1
        while i < len(make_answer):
            operator = make_answer[i]
            next_number = make_answer[i + 1]
            if operator == '+':
                resualt += next_number
            elif operator == '-':
                resualt -= next_number
            elif operator == '*':
                resualt *= next_number
            elif operator == '/':
                resualt /= next_number
            i = i + 2
#выводим полученный результат
        pin = list(final)
        i = 0
        help_vivod = ""
        vivod = ""
        now_symb = ""
        for i in range (len(pin)):
            h = pin[i]
            help_vivod +=(str(h))
            i = i+1
        pun = list(help_vivod)
        i = 0
        for i in range(len(pun)):
            if pun[i]!= '.':
                vivod += " "
                vivod += pun[i]
            else:
                vivod += pun[i]
                vivod += " "
            i = i + 1
        print(final,"=",resualt)'''
        
#для ошибки
        x = 1
        return x
    else:
        x = 0
        return x
def DaSHkins_you_are():
    global now_answer
    if any(yo in user_message for yo in you) :
        if any(bad in user_message for bad in bad_words):
            D = random.choice(DaSHkins_bad)
            G = D
            now_answer += G
        elif any(good in user_message for good in good_words):
            D = random.choice(DaSHkins_good)
            G = D
            now_answer += G
        x = 1
        return x
    else:
        x = 0
        return x
def chatting_history():
    if user_message in ["история разговора","история диалога"]:
        print("~ История нашего разговора ~")
        print()
        print(user_messages)
        print()
        print("Что писал я - пока не знаю...")
        x = 1
        return x
    else:
        x = 0
        return x
def DaSHkins_vopros():
    if any(what in user_message for what in whatP):
        G = random.choice(whatD)
        global now_answer
        now_answer += G
        x = 1
        return x
    else:
        x = 0
        return x
def DaSHkins_error():
    print(random.choice(errorD))
#список сообщений пользователя
user_messages = ""
#список ответов бота
DaSHkins_answers = ""
# Основа основ----------------------
while True:
# считаем ошибки
    error = 0
    # сообщение пользователя
    print() 
    pr = input("ваше сообщение: ").lower()
    #сохраняем в переменную сообщение пользователя
    user_message = ""
    user_perfect = pr.replace('ё','е')
    user_message += user_perfect
    #добавляем текущее сообщение пользователя в список всех его сообщений
    user_messages +='''
    '''
    user_messages += "Твоё сообщение: "
    user_messages += user_message
    user_messages += '''
    '''
    #создаём тeкущий ответ DaSHkins ввиде переменной
    now_answer = ""
    #создаём тeкущие ответы DaSHkins ввиде переменной(все за раз)
    now_answers = ""
    #здесь зачем-то рзбиваем сообщение пользователя на слова
    user_words = user_message.split()
    #считаем количество сообщений пользователя
    messages_quantity = messages_quantity + 1
    #создаем переменную для ответа бота
    # думает
    DaSHkins_thinking()
    #вывод истории разговора
    xread = chatting_history()
    if xread == 1:
        error = error + 1
    # Анализирует
    xread = DaSHkins_math()
    if xread == 1:
        error = error+1
    xread = DaSHkins_kto_ti()
    if xread == 1:
        error = error + 1
    xread = DaSHkins_poka()
    if xread == 1:
        error = error + 1
    xread = DaSHkins_function()
    if xread == 1:
        error = error+1
    xread = DaSHkins_greatings()
    if xread == 1:
        error = error+1
    xread = DaSHkins_neponyatno()
    if xread == 1:
        error = error + 1
    xread = DaSHkins_nesoglasen()
    if xread == 1:
        error = error + 1
    xread = DaSHkins_da()
    if xread == 1:
        error = error + 1
    xread = DaSHkins_sad()
    if xread == 1:
        error = error + 1
    xread = DaSHkins_lich()
    if xread == 1:
        error = error+1
    xread = time_of_day()
    if xread == 1:
        error = error + 1
    xread = DaSHkins_imba()
    if xread == 1:
        error = error+1
    xread = DaSHkins_blagodarnost()
    if xread == 1:
        error = error + 1
    xread = DaSHkins_ponyatno()
    if xread == 1:
        error = error + 1
    xread = DaSHkins_cho_delal()
    if xread == 1:
        error = error + 1
    xread = DaSHkins_OGO()
    if xread == 1:
        error = error+1
    xread = DaSHkins_you_are()
    if xread == 1:
        error = error + 1
        xread = DaSHkins_vopros()
    if xread == 1:
        error = error + 1
    # количество сообщений пользователя в чате(костыль)
    xread = user_messages_more()
    if xread == 1:
        error = error + 1
    #количество символов в сообщении пользователя
    '''User_messages_lenght()'''
    #добавляем текущий ответ бота в список всех его ответов
    now_answers += now_answer
    DaSHkins_answers += now_answers
    #выводим окончательный ответ DaSHkins
    print(now_answers)
    # количество сообщений пользователя в чате(вывод)
#проверка на ошибку
    if error == 0:
        print(random.choice(errorD))
    elif any(podg in user_message for podg in podgP):
        print()
