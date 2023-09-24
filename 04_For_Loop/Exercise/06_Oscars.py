# Поканени сте от академията да напишете софтуер, който да пресмята точките за актьор/актриса. Академията ще ви даде първоначални точки за актьора. След това всеки оценяващ ще дава своята оценка. Точките, които актьора получава се формират от: дължината на името на оценяващия умножено по точките, които дава делено на две.

# Ако резултатът в някой момент надхвърли 1250.5 програмата трябва да прекъсне и да се отпечата, че дадения актьор е получил номинация.

# Вход

# • Име на актьора - текст

# • Точки от академията - реално число в интервала [2.0... 450.5]

# • Брой оценяващи n - цяло число в интервала[1… 20]

# На следващите n-на брой реда:

# o Име на оценяващия - текст

# o Точки от оценяващия - реално число в интервала [1.0... 50.0]

# Изход

# Да се отпечата на конзолата един ред:

# · Ако точките са над 1250.5:

# "Congratulations, {име на актьора} got a nominee for leading role with {точки}!"

# · Ако точките не са достатъчни:

# "Sorry, {име на актьора} you need {нужни точки} more!"

# Резултатът да се форматирана до първата цифра след десетичния знак! 

actor = input()
academy_points = float(input())
raters = int(input())

total_points = 0

for _ in range(raters):
    rater_name = input()
    rater_points = float(input())

    rater_points = ((len(rater_name) * rater_points) / 2)
    total_points += rater_points

    if total_points+academy_points > 1250.50:
        print(f"Congratulations, {actor} got a nominee for leading role with {total_points+academy_points:.1f}!")
        break
    

diff = abs(1250.50 - (total_points + academy_points))
if total_points+academy_points < 1250.50:
    print(f"Sorry, {actor} you need {diff:.1f} more!")



