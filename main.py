import json # импорт модуля json для работы с json-файлами
# открытие файла flowers.json в режиме чтения с кодировкой utf-8
with open("flowers.json", 'r', encoding = 'utf-8') as file:  
    data = json.load(file) # загрузка данных из файла в переменную data
count = 0
actions_list = [
    ---------------------------
    "Вывести все записи",
    "Вывести запись по полю",
    "Добавить запись",
    "Удалить запись по полю",
    "Выйти из программы"
    ---------------------------
]
actions_count = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}
while True:
    print("""
    1: Вывести все записи
    2: Вывести запись по полю
    3: Добавить запись
    4: Удалить запись по полю
    5: Выйти из программы
""")
    num = int(input("Введите номер выбранного пункта: "))
    if num == 1:
        for flowers in data:
            print(f"""
            Номер записи: {flowers["id"]}
            Название: {flowers["name"]}
            Латинское название: {flowers["latin_name"]}
            Красная книга: {"да" if flowers["is_red_book_flower"] == True else "нет"}
            Цена(1 шт): {flowers["price"]}
        """)
        count += 1
        actions_count[1] +=1 
    elif num == 2:
        find = False
        id = input("Введите номер записи: ").strip()
        while not id.isdigit:
            print("Введено некорреткное значение")
            id = input("\nВведите номер записи: ")
        for flower in data:
            if id == flower.get("id",0):
                print(f"""
                    Номер записи: {flower["id"]}
                    Название: {flower["name"]}
                    Латинское название: {flower["latin_name"]}
                    Красная книга: {"да" if flower["is_red_book_flower"] == True else "нет"}
                    Цена(1 шт): {flower["price"]}          
                """)
                find = True
                break
        count += 1
        actions_count[2]+=1
    elif num == 3:
        find = False
        id = input("Введите новый номер записи: ").strip()
        while not id.isdigit:
            print("Введено некорректное значение. Повторите попытку: ")
            id = int(input("Введите новый номер записи: "))
        for flower in data:
            if flower.get("id",0) == id:
                find = True
                break
        if find:
             print("Такой номер уже существует")
             find = True
             break
        else:
            new_name = input("Введите название: ")
            new_latin_name = input("Введите латинское название цветка или '-': ")
            new_is_redbook_flower = input("Является ли краснокнижным(да/нет): ")
            flag = False 
            if new_is_redbook_flower.isdigit:
                flag = True
            while new_is_redbook_flower not in ["да", "нет"] or find:
                print("Введены неверные данные, повторите попытку")
                new_is_redbook_flower = input("Является ли краснокнижным(да/нет): ")
                if new_is_redbook_flower.isdigit:
                    flag = True
                    continue
                new_is_redbook_flower = new_is_redbook_flower.lower().strip()
                flag = False
            new_price = input("Введите цену за 1 шт: ")
            if not new_price.isdigit():
                while not new_price.isdigit():
                    print("Введено неверное значение!")
                    print("\nПовторите попытку!")
                    new_price = input("Введите цену за 1 шт: ")
                new_price = float(new_price)
            new_flower = {
                "id": id,
                "name": new_name,
                "latin_name":new_latin_name,
                "is_red_book_flower": True if new_is_redbook_flower.lower() == "да" else False,
                "price": new_price
            }
            data.append(new_flower)
            with open("flowers.json", 'w', encoding = 'utf-8') as out_file:
                json.dump(data, out_file)
            print("\nНовая запись успешно добавлена :)")
        count+=1
        actions_count[3]+=1
    elif num == 4:
        id = input("Введите номер записи, которую желаете удалить: ")
        while not id.isdigit:
            print("Введено неверное значение!")
            input("Введите номер записи ещё раз: ")
        find = False
        for flower in data:
            if flower.get("id", 0) == id:
                data.remove(flower)
                find = True
                break
        if not find:
            print("Запись не найдена.")
        with open("flowers.json", 'w', encoding = 'utf-8') as out_file:
            json.dump(data, out_file)
            print("\nЗапись успешно удалена.")
        count+=1
        actions_count[4]+=1
    elif num == 5:
        count+=1
        actions_count[5]+=1
        print(f"""\nПрограмма завершена. 
              \nОбщее количество выполненных операций: {count}""")
        print("\nСводка информации о каждом действии: ")
        count = 1
        for action in actions_list:
            print(f"""
                  {action}: {actions_count[count]}""")
            count +=1
        break
    else: 
        print("Такого номера нет.")
