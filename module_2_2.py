first = int(input('Введите 1ое целое число: '))
second = int(input('Введите 2ое целое число: '))
third =  int(input('Введите 3е целое число: '))
if first == second == third:
    print('Все' , 3, 'числа равны между собой' )
elif first == second or first == third or second == third:
    print( 2, 'числа равны между собой')
else:
    print('найдено', 0, 'чисел равных между собой ')
