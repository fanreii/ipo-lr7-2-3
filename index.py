import json
def ShowMainMenu():
    menu = """\n
---------------------------------
1. Вывести все записи
2. Вывести запись по полю
3. Добавить запись
4. Удалить запись по полю
5. Выйти из программы 
---------------------------------
"""
    return menu
def showInfo(data, flower_id=0):
    for flower in data:
        if flower_id == 0:
            print(f"""
            Номер записи: {flower["id"]},
            Название: {flower["name"]},
            Латинское название: {flower["latin_name"]},
            Красная книга: {f"да" if flower["is_red_book_flower"]  else "нет"},
            Цена(1 шт): {flower["price"]}
            """)
        else:
             if flower_id == flower.get("id"):
               print(f"""
                Номер записи: {flower["id"]}
                Название: {flower["name"]}
                Латинское название: {flower["latin_name"]}
                Красная книга: {f"да" if flower["is_red_book_flower"] else "нет"}
                Цена(1 шт): {flower["price"]}""")
def InputAndCheck():
    def ErrorMessage(value):
        print(f"""
              Введено недопустимое значение {value},
              Повторите попытку:\n""")
    def is_string(input_str):
            if isinstance(input_str, str) and (not input_str.isdigit()):
                return True
            ErrorMessage(input_str)
            return False
    def checkAnswer(answer):
            is_string(answer)
            if (answer.lower() == "да") or (answer.lower() == "нет"):
                return True
            else:
                ErrorMessage(answer)
                return False
    def turnToFloat(input_num):
        try:
            return True, float(input_num)
        except (ValueError, TypeError):
            ErrorMessage(input_num)
            return False, float("NaN")
    current_step = 1
    new_data = []
    while current_step < 5:
        if current_step == 1:
            new_name = input("Введите название нового цветка: ")
            new_data.append(new_name)
        elif current_step == 2:
            new_latin_name = input("Введите латинское название нового цветка: ")
            new_data.append(new_latin_name)
        elif current_step == 3:
            new_is_redbook_flower = input("Является ли цветком красной книги(да/нет): ")
            if not checkAnswer(new_is_redbook_flower):
                continue
            new_data.append(new_is_redbook_flower)
        elif current_step == 4:
            is_float, new_price = turnToFloat(input("Введите цену нового цветка: "))
            if not is_float:
                continue
            new_data.append(new_price)
        current_step += 1
    return new_data
def createNewFlower(id, name, latin_name, redbook, price):
    new_flower={
        "id":id,
        "name":name,
        "latin_name":latin_name,
        "is_red_book_flower":True if redbook.lower()=="да" else False,
        "price":price
    }
    return new_flower
def addNewFlower(data, new_flower):
    data.append(new_flower)

def deleteFlower(data, id, flag):
    for flower in data:
        if id == flower.get("id", 0):
            data.remove(flower)
            flag = True
            break
    return flag
def outprint(count, actions_list, actions_count):
    print(f"""
    Действия завершены
    Количество операций: {count}\n""")
    count=1
    print("Выполненные операции: ")
    for act in actions_list:
        print(f"""
        {act}: {actions_count[count]}""")
        count+=1
    return None
def checkId(id):
    while not id.isdigit():
        print("""Введено некорректное значение
              Повторите попытку:\n""")
        id = input("Введите номер желаемой записи: ")
    return id
with open("flowers.json", 'r', encoding = 'utf-8') as file:
    data = json.load(file)
count = 0
actions_list = [
    "Вывести все записи",
    "Вывести запись по полю",
    "Добавить запись",
    "Удалить запись по полю",
    "Выйти из программы"
]
actions_count = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}
while True:
    print(ShowMainMenu())
    num = int(input("Введите желаемый номер пункта: "))
    find = False
    if num ==1:
        showInfo(data)
        count+=1
        actions_count[1]+=1
    elif num ==2:
        id = input("Введите номер записи: ")
        id = checkId(id)
        for flower in data:
            if id == flower.get("id",0):
                showInfo(data, id)
                find =True
                break
        count+=1
        actions_count[2]+=1
        if not find:
            print("Такой записи не существует!")
    elif num ==3:
        find = False
        last_id = int(data[-1].get("id")) +1
        last_id = str(last_id)
        new_name, new_latin_name, new_is_redbook_flower, new_price = InputAndCheck()
        new_flower = createNewFlower(last_id, new_name, new_latin_name, new_is_redbook_flower, new_price)
        addNewFlower(data, new_flower)
        with open("flowers.json", 'w', encoding = 'utf-8') as outfile:
            json.dump(data, outfile)
        print("Новая запись успешно добавлена! :D")
        count+=1
        actions_count[3]+=1
    elif num ==4:
        id = input("Введите номер записи: ")
        id = checkId(id)
        find=False
        find=deleteFlower(data, id, find)
        if not find:
            print("Такой записи не существует")
        else:
            with open("flowers.json", 'w', encoding = 'utf-8') as outfile:
                json.dump(data, outfile)
            print("Запись успешно удалена")
        count+=1
        actions_count[4]+=1
    elif num == 5:
        count+=1
        actions_count[5]+=1
        outprint(count, actions_list, actions_count)
        break
    else:
        print("Такого номера нет!")