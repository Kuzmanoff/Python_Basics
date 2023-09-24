# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя, намира най-голямото измежду тях и го принтира. Въвежда се по едно число на ред

 

max_number = -10000000000000

while True:
    user_input = input()

    if user_input == "Stop":
        break

    
    number = int(user_input)

 
    if number > max_number:
        max_number = number

print(max_number)
