numbers = []
input_number = input("Введіть ціле число (для завершення введіть 0): ")

while input_number != "0":
    if input_number.isdigit():
        number = int(input_number)
        numbers.append(number)
    else:
        print("Число має бути цілим.Введіть ціле число.")

    input_number = input("Введіть ціле число (для завершення введіть 0): ")

if not numbers:
    print("Ви не ввели жодного числа.")
else:
    suma = sum(numbers)
    average = suma / len(numbers)
    min_value = min(numbers)
    max_value = max(numbers)
    even_number = 0

    for num in numbers:
        if num % 2 == 0:
            even_number += 1

    odd_number = len(numbers) - even_number
    print("Сума чисел:", suma)
    print("Середнє арифметичне: ", average)
    print("Мінімальне значення: ", min_value)
    print("Максимальне значення: ", max_value)
    print("Кількість парних чисел: ", even_number)
    print("Кількість непарних чисел: ", odd_number)
