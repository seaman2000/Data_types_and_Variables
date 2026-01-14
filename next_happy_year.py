number = int(input())

while True:
    number += 1
    number_str = str(number)

    if len(set(number_str)) == len(number_str):
        break

print(number)