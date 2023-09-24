# Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си. При всяка решена задача той получава оценка. Програмата трябва да приключи прочитането на данни при команда "Enough" или ако Марин получи определения брой незадоволителни оценки. Незадоволителна е всяка оценка, която е по-малка или равна на 4.

# Вход

# · На първи ред - брой незадоволителни оценки - цяло число;

# · След това многократно се четат по два реда:

# o Име на задача – текст;

# o Оценка - цяло число в интервала [2…6]

# Изход

# · Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:

# o "Average score: {средна оценка}"

# o "Number of problems: {броя на всички задачи}"

# o "Last problem: {името на последната задача}"

# · Ако получи определеният брой незадоволителни оценки:

# o "You need a break, {брой незадоволителни оценки} poor grades."

# Средната оценка да бъде форматирана до втория знак след десетичната запетая. 

number_poor_grades = int(input())
flag = False
count_poor = 0
sum_grades = 0
count_grades = 0
last_problem = ''
input_line = input()

while input_line != "Enough":

    current_grade = int(input())
    if current_grade <= 4:
        count_poor += 1

    if count_poor == number_poor_grades:
        flag = True
        break

    count_grades += 1
    sum_grades = sum_grades + current_grade
    last_problem = input_line
    input_line = input()

if flag == True:
    print(f"You need a break, {count_poor} poor grades.")
else:
    avg_grade = sum_grades / count_grades
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {count_grades:}")
    print(f"Last problem: {last_problem}")
