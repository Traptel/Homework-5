number = int(input("Введіть число: "))

i = 1
while i * i < number:
    square = i * i
    print(f"{i} * {i} = {square}")
    i += 1
