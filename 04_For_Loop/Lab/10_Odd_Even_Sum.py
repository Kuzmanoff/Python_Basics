# Да се напише програма, която чете n-на брой цели числа, подадени от потребителя и проверява дали сумата от числата на четни позиции е равна на сумата на числата на нечетни позиции.

# · Ако сумите са равни да се отпечатат два реда: "Yes" и на нов ред "Sum = " + сумата;

# · Ако сумите не са равни да се отпечат два реда: "No" и на нов ред "Diff = " + разликата.

# Разликата се изчислява по абсолютна стойност.

number = int(input())
odd_sum = 0
even_sum = 0

for i in range(1,number + 1):
    current_number = int(input())

    if i % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

if odd_sum == even_sum:
    print('Yes')
    print(f'Sum = {odd_sum}')
else:
    diff_number = abs(odd_sum - even_sum)
    print('No')
    print(f'Diff = {diff_number}')

