n = 0
while not n:
    try:
        n = int(input("Введите количество билетов, которое желаете приобрести"))
        if n <= 0:
            n = 0
            raise ValueError("Количество билетов не может быть меньше 1")
    except ValueError as e:
        print("Введёное значение не корректно")
        n = 0
age_list = [ ]
i = 1
while len(age_list) != n:
    try:
        age = int(input(f"Введите возраст {i} - го посетителя"))
        if 0<age<100:
            age_list.append(age)
            i += 1
        else:
            raise ValueError("Стлько люди не живут")
    except ValueError as e:
        print("Введёное значение не корректно")
def price_ticket(age):
    if 0 < age	< 18:
        return 0
    elif 18 <= age <= 25:
        return 990
    elif 25 < age:
        return 1390
price_list = [ ]
for i in range(n):
    price_list.append(price_ticket(age_list[i]))
price = 0
for i in price_list:
    price += i
if n>3:
    price *= 0.9
    print("Вы получили скидку 10%!!!")
print(f"Ссумма к оплате {price} рублей")





