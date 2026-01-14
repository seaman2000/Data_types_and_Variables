number = int(input())

lst_specials = [5, 7, 11]
sum_of_digits = 0
for num in range(1, number + 1):
    string_of_num = str(num)
    for digit in string_of_num:
        sum_of_digits += int(digit)
    if sum_of_digits in lst_specials:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
    sum_of_digits = 0