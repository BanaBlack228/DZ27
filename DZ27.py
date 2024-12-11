import os

def collect_user_info():
    user_info_list = []

    for i in range(1, 4):
        print(f"Введите информацию для Пользователя {i}:")
        name = input("Имя: ")
        surname = input("Фамилия: ")
        phone = input("Телефон: ")

        user_info = f"Пользователь {i}:\nИмя - {name}\nФамилия - {surname}\nТелефон - {phone}\n"
        user_info_list.append(user_info)

    return user_info_list


def save_to_file(user_info_list, filename):
    with open(filename, 'w') as file:
        for user_info in user_info_list:
            file.write(user_info)
            file.write("---------------------\n")


def main():
    user_info_list = collect_user_info()
    save_to_file(user_info_list, 'users.txt')
    print("Информация успешно записана в файл users.txt.")


if __name__ == "__main__":
    main()

def create_numbers_file():
    if not os.path.exists('numbers'):
        os.makedirs('numbers')

    with open('numbers/numbers.txt', 'w') as file:
        for i in range(1, 11):
            file.write(f"{i} {11 - i}\n")


def main():
    create_numbers_file()
    print("Файл numbers.txt успешно создан в каталоге 'numbers'.")


if __name__ == "__main__":
    main()

def read_numbers_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


def calculate_sum_of_products(lines):
    total_sum = 0
    for line in lines:
        numbers = line.split()
        if len(numbers) == 2:
            num1 = int(numbers[0])
            num2 = int(numbers[1])
            total_sum += num1 * num2
    return total_sum


def extract_right_column(lines):
    right_column = []
    for line in lines:
        numbers = line.split()
        if len(numbers) == 2:
            right_column.append(numbers[1])
    return right_column


def write_results_to_file(result_sum, right_column, output_filename):
    with open(output_filename, 'w') as file:
        file.write(f"Сумма произведений: {result_sum}\n")
        file.write("Числа из правого столбца:\n")
        file.write("\n".join(right_column) + "\n")


def main():
    numbers_file = 'numbers/numbers.txt'
    results_file = 'numbers/numbers_result.txt'

    lines = read_numbers_file(numbers_file)

    sum_of_products = calculate_sum_of_products(lines)

    right_column_numbers = extract_right_column(lines)

    write_results_to_file(sum_of_products, right_column_numbers, results_file)

    print("Результаты успешно записаны в файл numbers_result.txt.")


if __name__ == "__main__":
    main()
