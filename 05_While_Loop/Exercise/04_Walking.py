# Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден. Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си. Напишете програма, която чете от конзолата по колко стъпки изминава тя всеки път като излиза през деня и когато

# постигне целта си да се изписва "Goal reached! Good job!" и колко стъпки повече е извървяла "{разликата между стъпките} steps over the goal!"

# Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките, които е извървяла докато се прибира. След което, ако не е успяла да постигне целта си, на конзолата трябва да се изпише: "{разликата между стъпките} more steps to reach goal." 

sum_steps = 0
goal_steps = 10000
input_line = input()
while input_line != "Going home":
    steps = int(input_line)
    sum_steps += steps
 
    if sum_steps >= goal_steps:
        break
 
    input_line = input()
 
if input_line == "Going home":
    steps_home = int(input())
    sum_steps += steps_home
 
diff = abs(goal_steps - sum_steps)
if sum_steps >= goal_steps:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")