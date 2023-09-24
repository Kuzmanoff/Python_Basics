# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере дали ще успее да събере необходимата сума. Тя спестява или харчи част от парите си всеки ден. Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.

# Вход

# От конзолата се четат:

# · Пари, нужни за екскурзията - реално число;

# · Налични пари - реално число.

# След това многократно се четат по два реда:

# · Вид действие – текст с две възможности: "spend" или "save";

# · Сумата, която ще спести/похарчи - реално число.

# Изход

# Програмата трябва да приключи при следните случаи:

# · Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:

# o "You can't save the money."

# o "{Общ брой изминали дни}"

# · Ако Джеси събере парите за почивката, на конзолата се изписва:

# o "You saved the money for {общ брой изминали дни} days." 

req_money = float(input())
avail_money = float(input())

days = 0
conseq_days = 0

while True:
    activity = input() # spend or save
    
    
    if activity == 'spend':
        money = float(input())
        avail_money = avail_money - money
        days += 1
        conseq_days += 1
        if avail_money < 0:
            avail_money = 0

    elif activity == 'save':
        money = float(input())
        avail_money = avail_money + money
        days += 1
        conseq_days = 0

    if conseq_days == 5:
        print("You can't save the money.")
        print(days)
        break
    if avail_money >= req_money:
        print(f"You saved the money for {days} days.")
        break