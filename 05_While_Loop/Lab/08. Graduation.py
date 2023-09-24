# Напишете програма, която изчислява средната оценка на ученик от цялото му обучение. На първия ред ще получите името на ученика, а на всеки следващ ред неговите годишни оценки. Ученикът преминава в следващия клас, ако годишната му оценка е по-голяма или равна на 4.00. Ако ученикът бъде скъсан повече от един път, то той бива изключен и програмата приключва, като се отпечатва името на ученика и в кой клас бива изключен.

# При успешно завършване на 12-ти клас да се отпечата :

# "{име на ученика} graduated. Average grade: {средната оценка от цялото обучение}"

# В случай, че ученикът е изключен от училище, да се отпечата:

# "{име на ученика} has been excluded at {класа, в който е бил изключен} grade"

# Стойността трябва да бъде форматирана до втория знак след десетичната запетая. 

student = input()
grade_counter = 0
year_counter = 0
failed_counter = 0

while True:
    grade = float(input())
    
    if grade < 4:
        failed_counter += 1

        if failed_counter > 1:
            current_year = year_counter + 1
            print(f"{student} has been excluded at {current_year} grade")
            break
    else:
        grade_counter += grade
        year_counter += 1
    
    if year_counter == 12:
        average_grade = grade_counter / 12
        print(f"{student} graduated. Average grade: {average_grade:.2f}")
        break
        