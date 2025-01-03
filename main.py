import numpy as np
import random

def get_matrix_input():
    """Запрашивает у пользователя размерность и элементы матрицы."""
    while True:
        try:
            rows = int(input("Введите количество строк: "))
            cols = int(input("Введите количество столбцов: "))
            if rows <= 0 or cols <= 0:
                raise ValueError("Размерность должна быть положительным числом.")
            break
        except ValueError as e:
            print(f"Ошибка: {e}")

    choice = input(
        "Хотите ввести элементы вручную или сгенерировать их?: "
        "\n1. Ручной ввод"
        "\n2. Генерация"
        "\nВвод:"
                   ).strip().lower()
    if choice == '1':
        print("Введите элементы матрицы построчно, разделяя пробелами:")
        matrix = []
        for i in range(rows):
            while True:
                try:
                    row = list(map(int, input(f"Строка {i + 1}: ").split()))
                    if len(row) != cols:
                        raise ValueError(f"Должно быть {cols} элементов.")
                    matrix.append(row)
                    break
                except ValueError as e:
                    print(f"Ошибка: {e}")
        return np.array(matrix)
    elif choice == '2':
        while True:
            try:
                min_val = int(input("Введите минимальное значение для генерации: "))
                max_val = int(input("Введите максимальное значение для генерации: "))
                if min_val > max_val:
                    raise ValueError("Минимальное значение не может быть больше максимального.")
                break
            except ValueError as e:
                print(f"Ошибка: {e}")
        matrix = np.random.randint(min_val, max_val + 1, size=(rows, cols))
        print("Сгенерированная матрица:")
        print(matrix)
        return matrix
    else:
        print("Неверные входные значения!")

def compare_matrices(matrix1, matrix2):
    return np.array_equal(matrix1, matrix2)

def find_element(matrix, value):
    result = np.where(matrix == value)
    if result[0].size > 0:
        return [(int(row), int(col)) for row, col in zip(result[0], result[1])]
    return [(-1, -1)]

def find_three_largest(matrix):
    flat = matrix.flatten()
    return sorted(flat, reverse=True)[:3]













def main():
    print("Добро пожаловать в программу для работы с двумерными массивами!")
    matrix = get_matrix_input()

    while True:
        print("\nМеню:")
        print("1. Сравнить два массива")
        print("2. Найти элемент в массиве")
        print("3. Найти три наибольших элемента")
        print("4. Сумма элементов главной диагонали")
        print("5. Сумма элементов побочной диагонали")
        print("6. Сумма элементов с четной суммой индексов")
        print("7. Отразить массив по вертикали")
        print("8. Вывести массив")
        print("9. Выход")

        choice = input("Выберите действие: ")
        if choice == "1":
            print("Введите второй массив для сравнения:")
            matrix2 = get_matrix_input()
            print("Массивы равны:" if compare_matrices(matrix, matrix2) else "Массивы не равны.")
        elif choice == "2":
            try:
                value = int(input("Введите искомое значение: "))
                positions = find_element(matrix, value)
                print("Позиции элемента:", positions)
            except ValueError:
                print("Ошибка: введите целое число.")
        elif choice == "3":
            print("Три наибольших элемента:", find_three_largest(matrix))
        elif choice == "4":
            print("Сумма главной диагонали:", sum_main_diagonal(matrix))
        elif choice == "5":
            print("Сумма побочной диагонали:", sum_secondary_diagonal(matrix))
        elif choice == "6":
            print("Сумма элементов с четной суммой индексов:", sum_even_index_elements(matrix))
        elif choice == "7":
            matrix = reflect_matrix_vertically(matrix)
            print("Массив отражен по вертикали.")
        elif choice == "8":
            print("Текущий массив:")
            print(matrix)
        elif choice == "9":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Ошибка: выберите корректный пункт меню.")

if __name__ == "__main__":
    main()
