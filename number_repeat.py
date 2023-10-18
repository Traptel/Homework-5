number_str = input("Введіть число: ")

has_duplicate = False

for i in range(len(number_str)):
    for j in range(i + 1, len(number_str)):
        if number_str[i] == number_str[j]:
            has_duplicate = True
            break

    if has_duplicate:
        break

if has_duplicate:
    print("Так, в числі є однакові цифри.")
else:
    print("Ні, в числі немає однакових цифр.")
