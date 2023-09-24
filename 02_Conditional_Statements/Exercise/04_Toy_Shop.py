# Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни. С парите, които ще спечели иска да отиде на екскурзия.

# Цени на играчките:

# · Пъзел - 2.60 лв.

# · Говореща кукла - 3 лв.

# · Плюшено мече - 4.10 лв.

# · Миньон - 8.20 лв.

# · Камионче - 2 лв.

# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена. От спечелените пари Петя трябва да даде 10% за наема на магазина. Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.

# Вход

# От конзолата се четат 6 реда:

# 1. Цена на екскурзията - реално число в интервала [1.00 … 10000.00]

# 2. Брой пъзели - цяло число в интервала [0… 1000]

# 3. Брой говорещи кукли - цяло число в интервала [0 … 1000]

# 4. Брой плюшени мечета - цяло число в интервала [0 … 1000]

# 5. Брой миньони - цяло число в интервала [0 … 1000]

# 6. Брой камиончета - цяло число в интервала [0 … 1000]

# Изход

# На конзолата се отпечатва:

# · Ако парите са достатъчни се отпечатва:

# o "Yes! {оставащите пари} lv left."

# · Ако парите НЕ са достатъчни се отпечатва:

# o "Not enough money! {недостигащите пари} lv needed."

# Резултатът трябва да се форматира до втория знак след десетичната запетая. 

import math

trip_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
teddy_count = int(input())
minion_count = int(input())
truck_count = int(input())

puzzle = 2.60 * puzzle_count
doll = 3 *doll_count
teddy = 4.10*teddy_count
minion = 8.20*minion_count
truck = 2*truck_count

toy_price = puzzle + doll + teddy + minion + truck
toy_qty = puzzle_count + doll_count + teddy_count + minion_count + truck_count

if toy_qty >= 50:
    toy_price = toy_price - (toy_price * 0.25)

toy_price = toy_price - (toy_price * 0.1)

diff = abs(toy_price - trip_price)

if toy_price >= trip_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")