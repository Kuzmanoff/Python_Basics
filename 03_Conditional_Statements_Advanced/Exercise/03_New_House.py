# Марин и Нели си купуват къща недалеч от София. Нели толкова много обича цветята, че Ви убеждава да напишете програма, която да изчисли колко ще им струва, за да засадят определен брой цветя и дали наличният бюджет ще им е достатъчен. Различните цветя са с различни цени:

# цвете Роза Далия Лале Нарцис Гладиола

# Цена на брой в лева 5 3.80 2.80 3 2.50

# Съществуват следните отстъпки:

# · Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;

# · Ако Нели купи повече от 90 Далии - 15% отстъпка от крайната цена;

# · Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;

# · Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;

# · Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.

# От конзолата се четат 3 реда:

# · Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";

# · Брой цветя - цяло число;

# · Бюджет - цяло число.

# Да се отпечата на конзолата на един ред:

# · Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";

# · Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".

# Сумата да бъде форматирана до втория знак след десетичната запетая. 

type_flowers = input()
count_flowers = int(input())
budget = int(input())
 
total_sum = 0
if type_flowers == "Roses":
    total_sum = 5 * count_flowers
    if count_flowers > 80:
        total_sum = total_sum * 0.9
elif type_flowers == "Dahlias":
    total_sum = 3.8 * count_flowers
    if count_flowers > 90:
        total_sum = total_sum * 0.85
elif type_flowers == "Tulips":
    total_sum = 2.8 * count_flowers
    if count_flowers > 80:
        total_sum = total_sum * 0.85
elif type_flowers == "Narcissus":
    total_sum = 3 * count_flowers
    if count_flowers < 120:
        total_sum = total_sum * 1.15
elif type_flowers == "Gladiolus":
    total_sum = 2.5 * count_flowers
    if count_flowers < 80:
        total_sum = total_sum * 1.20
 
diff = abs(total_sum - budget)
if budget >= total_sum:
    print(f"Hey, you have a great garden with {count_flowers} {type_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")