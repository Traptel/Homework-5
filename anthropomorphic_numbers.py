number = input("Введіть натуральне число: ")

if number.isdigit():
    number = int(number)

    if number > 0:
        for i in range(1, number + 1):
            product = i * i
            last_digits = int(str(product)[-len(str(i)):])

            if last_digits == i:
                print(f"{i} * {i} = {product}")
    else:
        print("Число має бути натуральним.")
else:
    print("Число введено некоректно.")
