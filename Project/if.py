number = 23
guess = int(input('Введите целое число : '))

if guess == number:
    print('Поздравляю, вы угадали,')
    print('(хотя и не выиграли никакого приза!)')
elif guess < number:
    print('Нет, это число немного меньше загаданного')
else:
    print('Нет, загаданное число немного меньше')

print('Завершено')