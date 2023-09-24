# Катерачи от цяла България се събират на групи и набелязват следващите върхове за изкачване. Според размера на групата, катерачите ще изкачват различни върхове.

# · Група до 5 човека – изкачват Мусала

# · Група от 6 до 12 човека – изкачват Монблан

# · Група от 13 до 25 човека – изкачват Килиманджаро

# · Група от 26 до 40 човека – изкачват К2

# · Група от 41 или повече човека – изкачват Еверест

# Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх.

# Вход

# От конзолата се четат поредица от числа, всяко на отделен ред:

# · На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]

# · За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]

# Изход

# Да се отпечатат на конзолата 5 реда, всеки от които съдържа процент между 0.00% и 100.00% с точност до втората цифра след десетичната запетая.

# · Първи ред - процентът изкачващи Мусала

# · Втори ред – процентът изкачващи Монблан

# · Трети ред – процентът изкачващи Килиманджаро

# · Четвърти ред – процентът изкачващи К2

# · Пети ред – процентът изкачващи Еверест 

number_of_groups = int(input())
total_number_of_climbers = 0

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for _ in range(number_of_groups):
    current_number_of_group = int(input())
    total_number_of_climbers += current_number_of_group

    if current_number_of_group <= 5:
        musala += current_number_of_group
    elif 6<= current_number_of_group <= 12:
        monblan += current_number_of_group
    elif 13<= current_number_of_group <= 25:
        kilimanjaro += current_number_of_group
    elif 26<= current_number_of_group <= 40:
        k2 += current_number_of_group
    elif current_number_of_group > 40:
        everest += current_number_of_group

musala_percent = musala / total_number_of_climbers * 100
monblan_percent = monblan / total_number_of_climbers * 100
kilimanjaro_percent = kilimanjaro / total_number_of_climbers * 100
k2_percent = k2 / total_number_of_climbers * 100
everest_percent = everest / total_number_of_climbers * 100

print(f'{musala_percent:.2f}%')
print(f'{monblan_percent:.2f}%')
print(f'{kilimanjaro_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{everest_percent:.2f}%')