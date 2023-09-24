# Напишете програма, която чете от конзолата цели числа, докато не се получи команда "stop". Да се намери сумата на всички въведени прости и сумата на всички въведени непрости числа. Тъй като по дефиниция от математиката отрицателните числа не могат да бъдат прости, ако на входа се подаде отрицателно число, да се изведе следното съобщение "Number is negative.". В този случай въведено число се игнорира и не се прибавя към нито една от двете суми, а програмата продължава своето изпълнение, очаквайки въвеждане на следващо число.

# На изхода да се отпечатат на два реда двете намерени суми в следния формат:

# · "Sum of all prime numbers is: {prime numbers sum}"

# · "Sum of all non prime numbers is: {nonprime numbers sum}"

in_put = input()

prime_sum = 0
no_prime_sum = 0

while in_put != 'stop':
    curr_n = int(in_put)

    if curr_n < 0:
        print("Number is negative.")
        in_put = input()
        continue
    counter = 0
    for i in range(1, curr_n+1):
        if curr_n % i == 0:
            counter += 1
    
    if counter == 2:
        prime_sum += curr_n
    else:
        no_prime_sum += curr_n
    
    in_put = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {no_prime_sum}")