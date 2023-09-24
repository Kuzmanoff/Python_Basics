# Ресторант отваря врати и предлага няколко менюта на преференциални цени:

# • Пилешко меню – 10.35 лв.

# • Меню с риба – 12.40 лв.

# • Вегетарианско меню – 8.15 лв.

# Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.

# Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката).

# Цената на доставка е 2.50 лв и се начислява най-накрая.

# Вход

# От конзолата се четат 3 реда:

# · Брой пилешки менюта – цяло число в интервала [0 … 99]

# · Брой менюта с риба – цяло число в интервала [0 … 99]

# · Брой вегетариански менюта – цяло число в интервала [0 … 99]

# Изход

# Да се отпечата на конзолата един ред: "{цена на поръчката}"

count_chicken = int(input())
count_fish = int(input())
count_vegetarian = int(input())

price_chicken = count_chicken * 10.35
price_fish = count_fish * 12.40
price_vegetarian = count_vegetarian * 8.15

total_price = price_chicken + price_fish + price_vegetarian
desert = total_price * 0.2
delivery = 2.50

final_price = total_price + desert + delivery
print(final_price)