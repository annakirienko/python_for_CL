a = float(input('По шкале от 0 до 10, напишите, насколько Вы устали: '))
if a < 0.7:
    print('Кажется, Вы совсем не устали.')
elif 0.7 <= a < 3.5:
    print('Наверное, вы еще полны сил.')
elif 3.5 <= a < 6.8:
    print('Вы средненько устали.')
elif 6.8 <= a < 8.0:
    print('Давайте поднажмем!')
elif 8.0 <= a <= 10:
    print('Вызовите скорую, человеку плохо!')
else:
    print('Так нельзя? ай-яй-яй...')

