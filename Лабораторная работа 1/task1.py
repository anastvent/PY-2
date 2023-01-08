import doctest


class Phone:
    def __init__(self, name: str, colour: str, weight: float) :
        """
        Создание и подготовка к работе объекта "Телефон"

        :param name:Название телефона
        :param colour:Цвет телефона
        :param weight: Вес телефона,кг

        Примеры:
        >>> phone = Phone("Huawei", "Black", 0.3)
        """
        if not isinstance(name, str):
            raise TypeError("Название телефона должно быть типа str")
        self.name = name

        if not isinstance(colour, str):
            raise TypeError("Цвет телефона должен быть типа str")
        self.color = colour

        if not isinstance(weight, float):
            raise TypeError("Вес телефона должен быть типа float")
        if weight <= 0:
            raise ValueError("Вес телефона должен быть больше 0 кг")
        self.weight = weight

    def on_or_off_flashlight(self, state: int) -> None:
        """
        Функция которая включает и выключает фонарик на телефоне
        :param state: 1 - включить фонарик, 0 - выключить фонарик
        Примеры:
        >>> phone = Phone("Huawei", "Black", 0.3)
        >>> phone.on_or_off_flashlight(1)
        """
        if not isinstance(state, int):
            raise TypeError("переменная state должная быть типа int")
        if state not in (0, 1):
            raise ValueError("state может принимать только два значения 0 - выключить фонарик, 1 - включить фонарик")
        ...
    def status_phone(self) -> bool:
            """
        Функция, которая проверяет включен или выключен телефон
        :return: False - телефон включен, True - телефон выключен
        Примеры:
        >>> phone = Phone("Huawei", "Black", 0.3)
        >>> phone.status_phone() #True
        """
    ...
class Bag:
    def __init__(self, colour: str, size: str):
        """
        Создание и подготовка к работе объекта "Сумка"
        :param colour: Цвет сумки
        :param size: Размер сумки

        Примеры:
         >>> bag = Bag("Black", "XXL")
        """
        if not isinstance(size, str):
            raise TypeError("Размер должен быть типа str")
        if size not in ("S", "M", "L", "XL","XXL"):
            raise ValueError(' Размер сумки может принимать только следующие  значения: "S", "M", "L", "XL", "XXL"' )
        self.size = size

    def open(self) -> None:
        """
        Функция, которая открывает сумку
        Примеры:
        >>> bag = Bag("black", "S")
        >>> bag.open()
        """
        ...

    def close(self) -> None:
        """
         Функция, которая закрывает сумку
          Примеры:
           >>> bag = Bag("black", "S")
           >>> bag.close()
         """
        ...

class Student:
    def __init__(self, name: str, age: int, average_score: (int, float)):
        """
        Создание и подготовка к работе объекта "Студент"
        :param name: Имя
        :param age: Возраст
        :param average_score: Средний балл студента
        Пример:
        >>> student = Student("Анастасия", 22, 4.86)
        """

        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = age

        if not isinstance(average_score, (int, float)):
            raise TypeError("Средний балл должен быть типа int или float")
        if average_score < 0:
            raise ValueError("Средний балл не должен быть отрицательным")
        self.average_score = average_score

    def is_student_adult(self) -> bool:
        """
        Функция, которая проверяет является ли студент совершеннолетним
        :return: Является ли студент совершеннолетним (>=18)
        Пример:
        >>> student = Student("Анастасия", 22, 4.86)
        >>> student.is_student_adult()
        """
        ...


    def is_excellent_student(self) -> bool:
        """
        Функция, которая определяет студент отличник или нет
        :return: Является ли студент отличником (average_score >= 4,5)
        Пример:
        >>> student= Student("Анастасия", 22, 4.86)
        >>> student.is_excellent_student()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

