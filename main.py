import json
import csv
import random
import time
import os

proverkasebya = {"Здоровье:": 100, "Степень опьянения:": 0, "Урон от удара:": 20}
doskaob = {"Первый квест:": "Охота на монстров", "Второй кветс:": "Сбор ресурсов"}
skokdeneg = 0
def pokazhar():
    print("Характеристики вашего героя:")
    for i in proverkasebya:
        print(f"{i}  {(proverkasebya[i])}")
        time.sleep(1)   
    print(f"У вас {skokdeneg} золотых")
    time.sleep(1)
def pokazkvest():
    print("На доске висят следующие квесты:")
    for i in doskaob:
        print(f"{i} {doskaob[i]}")
        time.sleep(1)
def kvestdost():
    oplata = 0
    komudost = random.randint(1,3)
    chtodost = random.randint(1,3)
    while True:
        if komudost == 1:
            zakazchik = "оружейнику"
            break
        elif komudost == 2:
            zakazchik = "магу"
            break
        elif komudost == 3:
            zakazchik = "броннику"
            break
    while True:
        if chtodost == 1:
            predmetdost = "еду"
            oplata = oplata + 800
            break
        elif chtodost == 2:
            predmetdost = "сырье"
            oplata = oplata + 1000
            break
        elif chtodost == 3:
            predmetdost = "оплату"
            oplata = oplata + 900
            break
    print(f"В этом квесте вам необходимо будет доставить {predmetdost} {zakazchik}")
    print(f"За это вы получите {oplata}")
    print("------------------------------------")
    time.sleep(1)

def save_data():
    data = {
        "proverkasebya": proverkasebya,
        "skokdeneg": skokdeneg
    }
    with open('data.json', 'w') as file:
        json.dump(data, file)

def delete_save():
    if os.path.exists('data.json'):
        os.remove('data.json')

def write_to_csv():
    fieldnames = ["Здоровье", "Золотые"]
    row = [proverkasebya["Здоровье:"], skokdeneg]

    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(fieldnames)
        writer.writerow(row)

while True:
    vipil = "Степень опьянения:"
    bablo = "Золотых:"
    napils = 10
    hpvip = "Здоровье:"
    hpvipiz = 25
    hpvipps = 15
    skokahp = proverkasebya[hpvip]
    uron = "Урон от удара:"
    print("Ты в таверне \"Таверна у Серёги\"")
    print("Действия на выбор:", "1.Проверить самочувствие", "2.Выпить эля", "3.Подслушивать разговоры",
          "4.Посмотреть на доску квестов", "5.Закончить игру", "6.Сохранить прогресс", sep="\n")
    print("------------------------------------")
    vbr = int(input("Чем заняться?:"))
    if vbr == 1:
        pokazhar()
        print("---------------------", "\n")
    elif vbr == 5:
        write_to_csv()
        exit()
    elif vbr == 6:
        save_data()
    elif vbr == 2:
        print("Вы выпили, день продолжается:)")
        print("------------------------------------")
        proverkasebya[vipil] += napils
        stepnap = proverkasebya[vipil]
        sit = random.randint(0,1)
        if stepnap >= 50:
            if sit == 0:
                print(" Пьяный, вы начали дебоширить, за что вас избили:(\n" , "Зато, вы протрезвели:)")
                proverkasebya[vipil] = 0
                proverkasebya[hpvip] -= hpvipiz
                skokavip = proverkasebya[vipil]
                print("Ваше здоровье: ", skokahp)
                print("Степень вашего опьянения: ", skokavip)
                print("------------------------------------")
                time.sleep(1)
            elif sit == 1:
                print(" Вы уснули пьяным:) Вы проспали всю ночь и проснулись на следующий день")
                proverkasebya[vipil] = 0
                proverkasebya[hpvip] += hpvipps
                skokahp = proverkasebya[hpvip]
                skokavip = proverkasebya[vipil]
                print("Ваше здоровье: ", skokahp)
                print("Степень вашего опьянения: ", skokavip)
                print("------------------------------------")
                time.sleep(1)
        else:
            continue
    elif vbr == 4:
        while True:
            pokazkvest()
            time.sleep(1)
            print("---------------------------")
            print("1. Отойти от доски", "2. Прочесть квест об охоте", "3. Прочесть квест о сборе ресурсов", sep="\n")
            print("---------------------------")
            time.sleep(1)
            kvvb = int(input("Выбрать квест или вернуться обратно?"))
            if kvvb == 1:
                break
            elif kvvb == 2:
                monster = random.randint(1, 3)
                mn = ""
                hpmn = 0.0
                oplata = 0
                if monster == 1:
                    mn = "гоблинов"
                    oplata = oplata + 100
                    hpmn = hpmn + 4.5
                elif monster == 2:
                    mn = "орка"
                    hpmn = hpmn + 7
                    oplata = oplata + 250
                elif monster == 3:
                    mn = "волков"
                    oplata = oplata + 175
                    hpmn = hpmn + 3
                print(f"В этом квесте вам нужно будет убить {mn}")
                print(f"За этот квест вы можете получить {oplata} золотых")
                print("------------------------------------")
                print("Согласиться на квест?")
                pdkv = input("Да или Нет?")
                if pdkv == "Да":
                    print("Вы отправляетесь на охоту!")
                    print("Прибыв на нужное место, вы видите цель вашей охоты")
                    print("Что делать: 1.Идти в бой или 2.Сбежать")
                    a = int(input("Вы выбираете?:"))
                    if a == 1:
                        print("Вы вступаете в бой!")
                        while hpmn != 0:
                            boi = input("Что делать? Бить или защищаться:")
                            if boi == "Бить":
                                udar = random.randint(1, 5)
                                if udar <= 3:
                                    print("Вы удачно атаковали!")
                                    hpmn = hpmn - 0.75
                                if udar > 3:
                                    print("Вас атакуют:(")
                                    skokahp = skokahp - 10
                        print("Вы победили!")
                        print(f"Вы получаете {oplata}")
                        skokdeneg = skokdeneg + oplata
                    elif a == 2:
                        break
                elif pdkv == "Нет":
                    print("Вы отказываетесь от квеста:(")
            elif kvvb == 3:
                sbor = random.randint(1, 3)
                skokasobr = random.randint(1, 3)
                skoksobr = 0
                oplata = 0
                sb = ""
                while True:
                    if sbor == 1:
                        sb = sb + "волшебных камней"
                        break
                    elif sbor == 2:
                        sb = sb + "цветов жизни"
                        break
                    elif sbor == 3:
                        sb = sb + "жемчужен мудрости"
                        break
                while True:
                    if skokasobr == 1:
                        skoksobr = skoksobr + 100
                        oplata = oplata + skoksobr
                        break
                    elif skokasobr == 2:
                        skoksobr = skoksobr + 500
                        oplata = oplata + skoksobr
                        break
                    elif skokasobr == 3:
                        skoksobr = skoksobr + 1000
                        oplata = oplata + skoksobr
                        break
                    skoksobr = skoksobr
                    sb = sb
                print(f"В этом квесте нам нужно {skoksobr} {sb}")
                print(f"За этот квест вы можете получить {oplata} золотых")
                print("------------------------------------")
                print("Согласиться на квест?")
                pdkv = input("Да или Нет?")
                if pdkv == "Да":
                    print("Вы отправляетесь на место сбора ресурсов!")
                    i = 1
                    while i != oplata:
                        print(f"Вы собрали {i} {sb}")
                        i += 1
                        time.sleep(1)
                    print("Вы - молодец! Вы собрали всё, что нужно было, так что квест окончен!")
                    print(f"Вы получаете {oplata}")
                    skokdeneg = skokdeneg + oplata
                    print("---------------------------")
                elif pdkv == "Нет":
                    print("Вы отказываетесь от квеста:(")