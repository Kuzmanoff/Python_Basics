# Да се напише програма, която чете текст (стринг), въведен от потребителя, и изчислява и отпечатва сумата от стойностите на гласните букви според таблицата по-долу:

# буква a e i o u

# стойност 1 2 3 4 5 

txt = input()
point = 0

for i in range(0,len(txt)):
    if txt[i] == 'a':
        point += 1
    if txt[i] == 'e':
        point += 2
    if txt[i] == 'i':
        point += 3
    if txt[i] == 'o':
        point += 4
    if txt[i] == 'u':
        point += 5
print(point)