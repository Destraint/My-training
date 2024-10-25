cont = 0
end = 0
print("""etude_2.py v0.1

Программа, которая переводит число в любую систему счисления от 2 до 36
""")
while end == 0:
    number = input("Введите ваше число: ")
    num_system_1 = int(input("Введите систему счисления вашего числа (от 2 до 36): "))
    num_system_2 = int(input("Введите систему счисления, в которую нужно перевести число (от 2 до 36): "))

    if num_system_1 < 2 or num_system_1 > 36 or num_system_2 < 2 or num_system_1 > 36:
        print("Неправильно указаны системы счисления")
        cont = 0
    else:
        cont = 1
        
    if cont == 1:
        dec_num = int(str(number), num_system_1)
        conv_num = ""
        
        while dec_num > 0:
            remain = dec_num % num_system_2
            if remain < 10:
                conv_num += str(remain)
            else:
                conv_num += chr(remain+55)
            dec_num = dec_num // num_system_2
        
        final_num = "".join(reversed(str(conv_num)))
        print(final_num)
        end = int(input("""Продолжить?
Да - 0
Нет - 1

"""))

print("Хорошего дня")
