# Отпечатайте на конзолата таблицата за умножение за числата от 1 до 10 във формат: "{първи множител} * {втори множител} = {резултат}".

for x in range (1,11):
    for y in range (1,11):
        result = x*y
        print(f'{x} * {y} = {result}')