# Магазин за плодове през работните дни работи на следните цени:

# плод banana apple orange grapefruit kiwi pineapple grapes

# цена 2.50 1.20 0.85 1.45 2.70 5.50 3.85

# През събота и неделя магазинът работи на по-високи цени:

# плод banana apple orange grapefruit kiwi pineapple grapes

# цена 2.70 1.25 0.90 1.60 3.00 5.60 4.20

# Напишете програма, която чете от конзолата следните три променливи, въведени от потребителя, и пресмята цената според цените от таблиците по-горе:

# · плод - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;

# · ден от седмицата - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;

# · количество (реално число).

# Резултатът да се отпечата закръглен с 2 цифри след десетичната точка. При невалиден ден от седмицата или невалидно име на плод да се отпечата "error". 

fruit = input()
day = input()
qty = float(input())

price_banana = 0
price_apple = 0
price_orange = 0
price_grapefruit = 0
price_kiwi = 0
price_pineapple = 0
price_grapes = 0

 
if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        if fruit == 'banana':
            print(f'{qty*2.50:.2f}')
        elif fruit == 'apple':
           print(f'{qty*1.20:.2f}')
        elif fruit == 'orange':
           print(f'{qty*0.85:.2f}')
        elif fruit == 'grapefruit':
            print(f'{qty*1.45:.2f}')
        elif fruit == 'kiwi':
           print(f'{qty*2.70:.2f}')
        elif fruit == 'pineapple':
           print(f'{qty*5.50:.2f}')
        elif fruit == 'grapes':
            print(f'{qty*3.85:.2f}')
        else:
            print('error')

elif day == 'Saturday' or day == 'Sunday':
        if fruit == 'banana':
            print(f'{qty*2.70:.2f}')
        elif fruit == 'apple':
           print(f'{qty*1.25:.2f}')
        elif fruit == 'orange':
           print(f'{qty*0.90:.2f}')
        elif fruit == 'grapefruit':
            print(f'{qty*1.60:.2f}')
        elif fruit == 'kiwi':
           print(f'{qty*3:.2f}')
        elif fruit == 'pineapple':
           print(f'{qty*5.60:.2f}')
        elif fruit == 'grapes':
            print(f'{qty*4.20:.2f}')
        else:
            print('error')
else:
    print('error')
