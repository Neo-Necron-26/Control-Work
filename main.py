














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
