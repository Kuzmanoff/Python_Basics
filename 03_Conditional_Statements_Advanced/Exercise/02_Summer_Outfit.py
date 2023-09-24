# Лятото е сезон с много променливо време и Виктор има нужда от вашата помощ. Напишете програма, която спрямо времето от денонощието и градусите да препоръча на Виктор какви дрехи да облече. Вашият приятел има различни планове за всеки етап от деня, които изискват и различен външен вид - може да ги видите от таблицата.

# От конзолата се четат точно два реда:

# · Градусите - цяло число;

# · Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening".

# Като изход да се отпечата на конзолата на един ред: "It's {градуси} degrees, get your {облекло} and {обувки}."

degrees = int(input())
time = input()

outfit = 0
shoes = 0

if 10 <= degrees <=18:
    if time == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif time == 'Afternoon' or time== 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif 18 < degrees <=24:
    if time == 'Morning' or time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins' 
    elif time == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif degrees >= 25:
    if time == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif time == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    elif time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")