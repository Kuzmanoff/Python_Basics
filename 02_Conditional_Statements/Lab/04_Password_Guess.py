# Да се напише програма, която чете парола (текст), въведена от потребителя 
# и проверява дали въведената парола съвпада с фразата "s3cr3t!P@ssw0rd". 
# При съвпадение да се изведе "Welcome". 
# При несъвпадение да се изведе "Wrong password!". 

password = input()

phrase = "s3cr3t!P@ssw0rd"

if password == phrase:
    print('Welcome')
else:
    print('Wrong password!')