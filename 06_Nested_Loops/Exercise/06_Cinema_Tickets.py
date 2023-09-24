# Вашата задача е да напишете програма, която да изчислява процента на билетите за всеки тип от продадените билети: студентски(student), стандартен(standard) и детски(kid), за всички прожекции. Трябва да изчислите и колко процента от залата е запълнена за всяка една прожекция.

# Вход

# Входът е поредица от цели числа и текст:

# · На първия ред до получаване на командата "Finish" - име на филма – текст

# · На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]

# · За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване на командата "End":

# o Типа на закупения билет - текст ("student", "standard", "kid")

# Изход

# На конзолата трябва да се печатат следните редове:

# · След всеки филм да се отпечата, колко процента от кино залата е пълна

# "{името на филма} - {процент запълненост на залата}% full."

# · При получаване на командата "Finish" да се отпечатат четири реда:

# o "Total tickets: {общият брой закупени билети за всички филми}"

# o "{процент на студентските билети}% student tickets."

# o "{процент на стандартните билети}% standard tickets."

# o "{процент на детските билети}% kids tickets." 

total_tickets = 0

count_student = 0
count_standard = 0
count_kid = 0

movie_npt = input()
while movie_npt != 'Finish':
    movie = movie_npt
    seats = int(input())

    ticket_npt = input()
    ticket_count = 0
    while ticket_npt != 'End':
        ticket_type = ticket_npt
        ticket_count += 1
        total_tickets += 1

        if ticket_type == 'student':
            count_student += 1
        elif ticket_type == 'standard':
            count_standard += 1
        elif ticket_type == 'kid':
            count_kid += 1

        if ticket_count == seats:
            break
        ticket_npt = input() #next ticket
    
    movie_percent = (ticket_count / seats) * 100
    print(f"{movie} - {movie_percent:.2f}% full.")
    movie_npt = input() #next movie 

percent_student = count_student / total_tickets * 100
percent_standard = count_standard / total_tickets * 100
percent_kid = count_kid / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")
