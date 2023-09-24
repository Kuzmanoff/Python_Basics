# Да се напише програма, която чете 2 * n-на брой цели числа, подадени от потребителя, и проверява дали сумата на първите n числа (лява сума) е равна на сумата на вторите n числа (дясна сума). При равенство печата "Yes, sum = " + сумата; иначе печата "No, diff = " + разликата. Разликата се изчислява като положително число (по абсолютна стойност). 

n = int(input())

left_sum = 0
right_sum = 0

for i in range(2 * n):
    num = int(input())
    if i < n:
        left_sum += num
    else:
        right_sum += num

diff = abs(left_sum - right_sum)

if diff == 0:
    print("Yes, sum =", left_sum)
else:
    print("No, diff =", diff)