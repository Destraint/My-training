class Human:
    def __init__(self, name, weight, height, age, gender, load):
        self.name = name
        self.weight = weight
        self.height = height
        self.gender = gender
        self.age = age
        self.load = load
    
    def print_info(self):
        print(f"Имя: {self.name} | Вес: {self.weight} | Рост: {self.height} | Возраст: {self.age} | Пол: {self.gender}")
        
    def BBO(self):
        BBO = self.weight*9.99 + self.height*6.25 - self.age*4.92
        if self.gender == "Мужской":
            BBO += 5
        elif self.gender == "Женский":
            BBO -= 161
        
        match self.load:
            case 1:
                BBO = BBO * 1.2
            case 2:
                BBO = BBO * 1.38
            case 3:
                BBO = BBO * 1.46
            case 4:
                BBO = BBO * 1.55
            case 5:
                BBO = BBO * 1.64
            case 6:
                BBO = BBO * 1.73
            case 7:
                BBO = BBO * 1.9
        print(f"Сколько нужно потреблять каллорий в день: {round(BBO, 2)}")
        
class Gym(Human):
    def card(self, cost):
        self.cost = cost
        
    def message(self):
        print(f"Здравствуйте, {self.name}. Вам нужно заплатить за абонемент в спортзал {self.cost} рублей до конца недели.")
person = Gym(input("Ваше имя: "), float(input("Ваш вес: ")), float(input("Ваш рост: ")), int(input("Ваш возраст: ")), input("Ваш пол: "), int(input("""Выберите из списка уровень вашей нагрузки:

1 - Физическая нагрузка отсутствует или минимальная
2 - Тренировки средней тяжести 3 раза в неделю
3 - Тренировки средней тяжести 5 раз в неделю
4 - Интенсивные тренировки 5 раз в неделю
5 - Тренировки каждый день
6 - Интенсивные тренировки каждый день или по 2 раза в день
7 - Ежедневная нагрузка + физическая работа
Ваша нагрузка: """)))

person.print_info()
person.card(18000)
person.message()
