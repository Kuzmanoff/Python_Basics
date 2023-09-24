# Фирма дава следните комисионни на търговците си според града, в който работят и обема на продажбите:

# Град 0 ≤ s ≤ 500 500 < s ≤ 1 000 1 000 < s ≤ 10 000 s > 10 000

# Sofia 5% 7% 8% 12%

# Varna 4.5% 7.5% 10% 13%

# Plovdiv 5.5% 8% 12% 14.5%

# Напишете конзолна програма, която чете име на град (текст) и обем на продажби (реално число), въведени от потребителя, и изчислява и извежда размера на търговската комисионна според горната таблица. Резултатът да се изведе форматиран до 2 цифри след десетичната точка. При невалиден град или обем на продажбите (отрицателно число) да се отпечата "error". 

city = input()
sales = float(input())

comission = 0

if city == 'Sofia': 
    if 0 <= sales <= 500:
        comission = 0.05
        print(f'{sales*comission:.2f}')
    elif 500 <= sales <= 1000:
        comission = 0.07
        print(f'{sales*comission:.2f}')
    elif 1000 <= sales <= 10000:
        comission = 0.08
        print(f'{sales*comission:.2f}')
    elif sales > 10000:
        comission = 0.12
        print(f'{sales*comission:.2f}')
    else:
        print('error')
elif city == 'Varna': 
    if 0 <= sales <= 500:
        comission = 0.045
        print(f'{sales*comission:.2f}')
    elif 500 <= sales <= 1000:
        comission = 0.075
        print(f'{sales*comission:.2f}')
    elif 1000 <= sales <= 10000:
        comission = 0.10
        print(f'{sales*comission:.2f}')
    elif sales > 10000:
        comission = 0.13
        print(f'{sales*comission:.2f}')
    else:
        print('error')
elif city == 'Plovdiv': 
    if 0 <= sales <= 500:
        comission = 0.055
        print(f'{sales*comission:.2f}')
    elif 500 <= sales <= 1000:
        comission = 0.08
        print(f'{sales*comission:.2f}')
    elif 1000 <= sales <= 10000:
        comission = 0.12
        print(f'{sales*comission:.2f}')
    elif sales > 10000:
        comission = 0.145
        print(f'{sales*comission:.2f}')
    else:
        print('error')
else:
    print('error')