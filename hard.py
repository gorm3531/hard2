import random
def result():
    num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    first_num = random.choice(num)
    i = 1
    print(first_num, '- ', end='')
    while i <= 20:
        i += 1
        j = 0
        while j <= 20:
            j += 1
            if i == j:
                break

            elif first_num == (i + j):
                print(f'{i}{j}', end='')
password = result()