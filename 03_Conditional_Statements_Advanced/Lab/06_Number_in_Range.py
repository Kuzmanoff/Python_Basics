# Да се напише програма, която проверява дали въведеното от потребителя число е в интервала [-100, 100] 
# и е различно от 0 и извежда "Yes", ако отговаря на условията, 
# или "No" ако е извън тях

num = int(input())

if -100 <= num <= 100 and num != 0:
    print("Yes")
else:
    print("No")
