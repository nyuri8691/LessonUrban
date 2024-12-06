number = int(input('Введите число от 3 до 20: '))

while 3 > number or number > 20:
    number = int(input('Число не в диапазоне от 3 до 20. Попробуйте ещё: '))
def get_result(number_):
    result = []

    for i in range(1, number_ + 1):
        for j in range(i + 1, number_ + 1):
            if number_ % (i + j) == 0:
                result.append(str(i))
                result.append(str(j))
    return result
res = get_result(number)

print('Ваш пароль:')
print(*res)
