def task2(mas):
    md = []
    for n in range(2, 1000):
        divisor = all(num % n == 0 for num in mas)
        if divisor:
            md.append(n)
    return md


def task3(mas3):

        if len(mas3) != 2:
            return "Введите два числа "
        min_num = min(mas3)
        max_num = max(mas3)
        print(f"Минимальное число: {min_num}")
        print(f"Максимальное число: {max_num}")
        prime_numbers = []
        for n in range(min_num, max_num + 1):
            if all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
                prime_numbers.append(n)
        return prime_numbers

def task4(num):
    num = int(num)
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            print(i * j, end=" ")
        print()


def menu():
    print("1. Задание №1")
    print("2. Задание №2")
    print("3. Задание №3")
    print("4. Задание №4")


while True:
    menu()
    choice = input('Выберете номер задания: ')
    if choice == '1':
        while True:
            comp = input('Введите число ')
            if comp == '':
                break
            comp = int(comp)
            if comp == 0:
                print(f'Введите числа от 1')
            elif comp == 1:
                print(f'{comp} компьютер')
            elif comp in range(2, 5):
                print(f'{comp} компьютера')
            elif comp >=5:
                print(f'{comp} компьютеров')

    if choice == '2':
        while True:
            mas = input('Введите массив чисел: ')
            if mas == '':
                break
            mas = [int(num) for num in mas.split()]
            result = task2(mas)
            print(result)
    if choice == '3':
        while True:
            mas3 = input('Введите массив чисел: ')
            if mas3 == '':
                break
            if len(mas3) != 2:
                print('Введите 2 числа')

            mas3 = [int(num) for num in mas3.split()]
            result1 = task3(mas3)
            print(result1)

    if choice == '4':
        while True:
            mas4 = input('Введите число ')
            if mas4 == '':
                break
            result2 = task4(mas4)
            print(result2)




