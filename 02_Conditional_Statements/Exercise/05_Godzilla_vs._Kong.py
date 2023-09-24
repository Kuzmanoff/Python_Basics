# Снимките за дългоочаквания филм "Годзила срещу Конг" започват. Сценаристът Адам Уингард ви моли да напишете програма, която да изчисли, дали предвидените средства са достатъчни за снимането на филма. За снимките ще бъдат нужни определен брой статисти, облекло за всеки един статист и декор.

# Известно е, че:

# · Декорът за филма е на стойност 10% от бюджета.

# · При повече от 150 статиста, има отстъпка за облеклото на стойност 10%.

# Вход

# От конзолата се четат 3 реда:

# Ред 1. Бюджет за филма – реално число в интервала [1.00 … 1000000.00]

# Ред 2. Брой на статистите – цяло число в интервала [1 … 500]

# Ред 3. Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]

# Изход

# На конзолата трябва да се отпечатат два реда:

# · Ако парите за декора и дрехите са повече от бюджета:

# o "Not enough money!"

# o "Wingard needs {парите недостигащи за филма} leva more."

# · Ако парите за декора и дрехите са по малко или равни на бюджета:

# o "Action!"

# o "Wingard starts filming with {останалите пари} leva left."

# Резултатът трябва да е форматиран до втория знак след десетичната запетая. 

budget = float(input())
count_statists = int(input())
clothing_price = float(input())

decor_price = budget * 0.10 

total_clothing = count_statists * clothing_price

if count_statists > 150:
    total_clothing = total_clothing * 0.90 

total_sum = decor_price + total_clothing

diff = abs(budget - total_sum)

if budget >= total_sum:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")