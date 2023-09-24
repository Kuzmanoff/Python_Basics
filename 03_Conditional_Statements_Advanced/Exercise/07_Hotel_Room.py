# Хотел предлага 2 вида стаи: студио и апартамент. Напишете програма, която изчислява цената за целия престой за студио и апартамент. Цените зависят от месеца на престоя:

# Май и октомври Юни и септември Юли и август

# Студио - 50 лв./нощувка Студио - 75.20 лв./нощувка Студио - 76 лв./нощувка

# Апартамент - 65 лв./нощувка Апартамент - 68.70 лв./нощувка Апартамент - 77 лв./нощувка

# Предлагат се и следните отстъпки:

# · За студио, при повече от 7 нощувки през май и октомври : 5% намаление.

# · За студио, при повече от 14 нощувки през май и октомври : 30% намаление.

# · За студио, при повече от 14 нощувки през юни и септември: 20% намаление.

# · За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.

# Вход

# Входът се чете от конзолата и съдържа точно 2 реда, въведени от потребителя:

# · На първия ред е месецът - May, June, July, August, September или October;

# · На втория ред е броят на нощувките - цяло число.

# Изход

# Да се отпечатат на конзолата 2 реда:

# · На първия ред: "Apartment: {цена за целият престой} lv."

# · На втория ред: "Studio: {цена за целият престой} lv."

# Цената за целия престой да е форматирана с точност до два знака след десетичната запетая. 

month = input()
count_nights = int(input())
 
apartment_price = 0
studio_price = 0
if month == "May" or month == "October":
    apartment_price = 65 * count_nights
    studio_price = 50 * count_nights
 
elif month == "June" or month == "September":
    apartment_price = 68.7 * count_nights
    studio_price = 75.2 * count_nights
 
elif month == "July" or month == "August":
    apartment_price = 77 * count_nights
    studio_price = 76 * count_nights
 
if count_nights > 14 and (month == "May" or month == "October"):
    studio_price = studio_price * 0.70
elif count_nights > 7 and (month == "May" or month == "October"):
    studio_price = studio_price * 0.95
elif count_nights > 14 and (month == "June" or month == "September"):
    studio_price = studio_price * 0.8
 
if count_nights > 14:
    apartment_price = apartment_price * 0.9
 
print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")