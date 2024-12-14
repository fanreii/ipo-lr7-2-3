- Написать программу, которая выводит меню выбора:
    - вывести все записи
    - вывести запись по полю
    - добавить запись
    - удалить  запись
    - выйти из программы
------------------------------------------------
- После выполнения пунктов меню (кроме “выйти из программы”) меню отображается снова
- Все записи хранятся в виде .json файла
- Пункт “Вывести все записи” — выводит в форматированном виде все записи из файла
- Пункт “Вывести запись по полю” — выводит одну запись по определённому полю (поле id), а так же ее позицию в словаре.
- Пункт “Добавить запись” — запрашивает у пользователя нужные данные и добавляет запись в файл
- Пункт “Удалить запись по полю” — удаляет запись из файла по определенному полю  (поле id)
- Пункт “Выйти из программы” — завершает выполнение программы, но перед этим вводит на экран количество выполненных операций с записями
- Пункты “Вывести запись по полю” и “Удалить запись по полю” должны выводить предупреждение если нужная запись не найдена
------------------------------------------------- 
- Файл json должен иметь вид:
  - id/ номер записи
  - name/ общее название цветка
  - latin_name/ латинское(научное) название цветка
  - is_red_book_flower/ булевый тип данных, указывающий на то, является ли цветок краснокнижным
  - price/ стоимость цветка
--------------------------------------------------
