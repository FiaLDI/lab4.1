class Conversation:
    def __init__(self, first, second):
        """
        Инициализатор класса Conversation.
        first: продолжительность телефонного разговора в минутах (целое положительное число)
        second: стоимость одной минуты в рублях (дробное положительное число)
        """
        if not isinstance(first, int) or first <= 0:
            raise ValueError("Поле 'first' должно быть целым положительным числом.")
        if not isinstance(second, (int, float)) or second <= 0:
            raise ValueError("Поле 'second' должно быть положительным числом.")
        
        self.first = first
        self.second = second

    def cost(self):
        """Вычисление общей стоимости разговора"""
        return self.first * self.second

    def display(self):
        """Вывод данных на экран"""
        print(f"Продолжительность разговора: {self.first} минут")
        print(f"Стоимость одной минуты: {self.second} рубля")
        print(f"Общая стоимость разговора: {self.cost()} рублей")

    def read(self):
        """Ввод данных с клавиатуры"""
        try:
            self.first = int(input("Введите продолжительность разговора в минутах (целое положительное число): "))
            self.second = float(input("Введите стоимость одной минуты в рублях (положительное число): "))
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
            return None


def make_Conversation(first, second):
    """
    Внешняя функция для создания объекта Conversation.
    Проверяет корректность переданных параметров.
    """
    try:
        return Conversation(first, second)
    except ValueError as e:
        print(f"Ошибка создания объекта: {e}")
        return None


# Пример использования
if __name__ == "__main__":
    # Создание объекта через функцию make_Conversation
    conv = make_Conversation(10, 2.5)
    if conv:
        conv.display()
        conv.read()
        conv.display()
