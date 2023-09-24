# Напишете програма която, чете ден от седмицата (текст), на английски език - въведен от потребителя.
# Ако денят е работен отпечатва на конзолата - "Working day", ако е почивен - "Weekend". 
# Ако се въведе текст различен от ден от седмицата да се отпечата - "Error". 

weekday = input()

if weekday == 'Monday':
    print('Working day')
elif weekday == 'Tuesday':
    print('Working day')
elif weekday == 'Wednesday':
    print('Working day')
elif weekday == 'Thursday':
    print('Working day')
elif weekday == 'Friday':
    print('Working day')
elif weekday == 'Saturday':
    print('Weekend')
elif weekday == 'Sunday':
    print('Weekend')
else:
    print('Error')