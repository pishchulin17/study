username = input("Введите ваше имя:\n")
age = int(input("Введите ваш возраст:\n"))
print(f"Добрый день, {username}!")
if age > 17:
    print('Вы можете открыть вклад.')
    deposit = int(input("Какую сумму вы хотите внести?\n"))
    if 50000 > deposit >= 10000:
        percent = 3
        total = (deposit * 1.03)
        print(f"Спасибо за то, что воспользовались нашими услугами, {username}!")
        print(f"Вы вложили {deposit}, ставка составляет {percent}%.")
        print(f"В конце года вы можете забрать {total:.2f} рублей.")
    elif 100000 > deposit > 50000:
        percent = 4
        total = (deposit * 1.04)
        print(f"Спасибо за то, что воспользовались нашими услугами, {username}!")
        print(f"Вы вложили {deposit}, ставка составляет {percent}%.")
        print(f"В конце года вы можете забрать {total:.2f} рублей.")
    elif deposit >= 100000:
        percent = 5
        total = (deposit * 1.05)
        print(f"Спасибо за то, что воспользовались нашими услугами, {username}!")
        print(f"Вы вложили {deposit}, ставка составляет {percent}%.")
        print(f"В конце года вы можете забрать {total:.2f} рублей.")
    else:
        print(f'Извините, до минимальной суммы вклада вам не хватает {10000 - deposit} рублей')
elif 13 < age < 18:
    print(f'Вам ещё рано открывать вклад. Приходите через {18 - age} года.')
else:
    print(f'Вам ещё рано открывать вклад. Приходите через {18 - age} лет.')
