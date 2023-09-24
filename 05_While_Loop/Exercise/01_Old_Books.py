# Ани отива до родния си град след много дълъг период извън страната. Прибирайки се вкъщи, тя вижда старата библиотека на баба си и си спомня за любимата си книга. Помогнете на Ани, като напишете програма, в която тя въвежда търсената от нея книга (текст). Докато Ани не намери любимата си книга или не провери всички книги в библиотеката, програмата трябва да чете всеки път на нов ред името на всяка следваща книга (текст), която тя проверява. Книгите в библиотеката са свършили щом получите текст "No More Books".

# · Ако не открие търсената книгата да се отпечата на два реда:

# o "The book you search is not here!"

# o "You checked {брой} books."

# · Ако открие книгата си се отпечатва един ред:

# o "You checked {брой} books and found it." 

book = input()
counter = 0
next_book = ''

while True:

    if next_book != book:
        next_book = input()
        counter += 1
    else:
        print(f"You checked {counter-1} books and found it.")
        break

    if next_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {counter-1} books.")
        break
    
    