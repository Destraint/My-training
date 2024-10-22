word = input("Напиши слово или предложение: ")

num = int(input("""-----------------------
Выбери нужную операцию из списка:
-----------------------
Количество символов - 1
Количество символов без пробелов - 2
Перевести все символы в верхний регистр - 3
Перевести все символы в нижний регистр - 4
Перевести первый символ в верхний регистр, остальные в нижний - 5
Количество определённого символа в строке - 6
-----------------------
Операция: """))
print("-----------------------")
match num:
    case 1:
        print(f"Количество символов: {len(word)}")
    case 2:
        print(f"Количество символов без пробелов: {len(word)-word.count(" ")}")
    case 3:
        print(word.upper())
    case 4:
        print(word.lower())
    case 5:
        print(word.capitalize())
    case 6:
        sym = input("Какой символ нужно подсчитать: ")
        print("-----------------------")
        print(word.count(sym))