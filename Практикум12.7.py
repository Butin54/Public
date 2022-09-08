per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада"))
per_cent_list = list (map ( float , per_cent.values()))
deposit = [per_cent_list[0]*money/100 , per_cent_list[1]*money/100 , per_cent_list[2]*money/100 , per_cent_list[3]*money/100]
print(deposit)
print("Максимальная сумма, которую вы можете заработать -", max(deposit), "rub")
