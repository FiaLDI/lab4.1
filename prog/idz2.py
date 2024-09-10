#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Cursor:
    def __init__(self, x=1, y=1, view="horizontal", size=1):
        if not (1 <= x <= 100) or not (1 <= y <= 100):
            raise ValueError("Координаты - целыми числами от 1 до 100.")
        if view not in ["horizontal", "vertical"]:
            raise ValueError(
                "Вид курсора должен быть 'horizontal' или 'vertical'."
            )
        if not (1 <= size <= 15):
            raise ValueError(
                "Размер курсора должен быть целым числом от 1 до 15."
            )

        self.x = x  # Координата по горизонтали
        self.y = y  # Координата по вертикали
        self.view = view  # Вид курсора
        self.size = size  # Размер курсора
        self.visible = True  # Флаг видимости курсора

    def read(self):
        self.x = int(input("Введите координату по горизонтали (1-100): "))
        self.y = int(input("Введите координату по вертикали (1-100): "))
        self.view = input(
            "Введите вид курсора ('horizontal' или 'vertical'): "
        )
        self.size = int(input("Введите размер курсора (1-15): "))

    def display(self):
        if self.visible:
            print(
                f"Курсор на координатах ({self.x}, {self.y}), "
                f"вид: {self.view}, размер: {self.size}."
            )
        else:
            print("Курсор скрыт.")

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
        print(f"Курсор перемещён на ({delta_x}, {delta_y}).")

    def change_view(self, new_view):
        if new_view in ["horizontal", "vertical"]:
            self.view = new_view
            print(f"Вид курсора изменён на: {self.view}.")
        else:
            print("Некорректный вид курсора.")

    def change_size(self, new_size):
        if 1 <= new_size <= 15:
            self.size = new_size
            print(f"Размер курсора изменён на: {self.size}.")
        else:
            print("Некорректный размер курсора.")

    def hide(self):
        self.visible = False
        print("Курсор скрыт.")

    def show(self):
        self.visible = True
        print("Курсор восстановлен.")


def main():
    # Демонстрация возможностей класса Cursor
    cursor = Cursor()  # Создаем курсор с начальными значениями
    cursor.display()  # Выводим информацию о курсоре

    # Вводим новые значения для курсора
    cursor.read()
    cursor.display()

    # Перемещение курсора
    cursor.move(5, 3)
    cursor.display()

    # Изменение вида и размера курсора
    cursor.change_view("vertical")
    cursor.change_size(10)
    cursor.display()

    # Скрытие и восстановление курсора
    cursor.hide()
    cursor.display()
    cursor.show()
    cursor.display()


if __name__ == "__main__":
    main()
