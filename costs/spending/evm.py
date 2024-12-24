def plus(a, b):
    a = '0' + a[0] + a.split('.')[0] + a.split('.')[1]
    b = '0' + b[0] + b.split('.')[0] + b.split('.')[1]
    k = 0
    s = ''
    for i in range(len(a) - 1, -1, -1):
        s = str(int(a[i]) ^ int(b[i]) ^ k) + s
        k = (int(a[i]) & int(b[i])) | (int(a[i]) & k) | (int(b[i]) & k)
    s = s[0:3] + '.' + s[3:]
    return s


def PinO(a):  # получается работает в обе стороны
    if a[0] == '0':
        return a
    else:
        s = '1.'
        for i in a[2:]:
            if i == '0':
                s += '1'
            else:
                s += '0'
        return s


def PinD(a):
    if a[0] == '0':
        return (a)
    else:
        s = PinO(a)
        s = plus(s, '0.' + '0' * (len(s) - 3) + '1')
        if (s[1:3] != '11') and (s[1:3] != '00'):
            return 'Overflow'
        return s[2:]


def OinD(a):
    if a[0] == '0':
        return (a)
    else:
        s = plus(a, '0.' + '0' * (len(a) - 3) + '1')
        if (s[1:3] != '11') and (s[1:3] != '00'):
            return 'Overflow'
        return s[2:]


def DinP(a):
    if a[0] == '0':
        return a
    for i in range(len(a) - 1, 1, -1):
        if a[i] == '1':
            c = i
            break
    a = a[:c] + '0' + '1' * (len(a) - c - 1)
    a = PinO(a)
    return a


def DinO(a):
    if a[0] == '0':
        return a
    for i in range(len(a) - 1, 1, -1):
        if a[i] == '1':
            c = i
            break
    a = a[:c] + '0' + '1' * (len(a) - c - 1)
    return a


def denormmin(x1, x2, y2):
    print('Необходима денормализация мантиссы, сместим ее на порядок вправо')
    x2, y2 = PinO(x2), PinO(y2)
    x2, y2 = x2[:2] + '0' + x2[2:], y2[:2] + '0' + y2[2:]
    x2, y2 = PinO(x2), PinO(y2)

    if x1 != ('0.' + '1' * (len(x1) - 2)):
        ed = '0.' + '0' * (len(x1) - 3) + '1'
        x1 = PinD(x1)
        ed = PinD(ed)
        x1 = plus(x1, ed)[2:]
        x1 = DinP(x1)
    else:
        x1 = '0.1' + '0' * (len(x1) - 2)

    print('Увеличенный порядок: ', x1)
    print('Мантисса первого в мoк: ', x2[0] + x2)
    print('Мантисса второго в мoк: ', y2[0] + y2)
    print(' ', x2[0] + x2)
    print('+')
    print(' ', y2[0] + y2)
    s = plus(x2, y2)
    print('-------------')
    print(' ', s)
    if s[0] == '1':
        print('\n')
        print(' ', s[1:])
        print('+')
        print(' ', '00.' + '0' * (len(s[1:]) - 4) + '1')
        s = plus(s[2:], '0.' + '0' * (len(s[1:]) - 4) + '1')
        print('-------------')
        print(' ', s)
    return [s[:-1], x1]


def denormplu(x1, x2, y2):
    print('Необходима денормализация мантиссы, сместим ее на порядок влево')
    x2, y2 = PinO(x2), PinO(y2)
    x2, y2 = x2[:2] + x2[3:] + '0', y2[:2] + y2[3:] + '0'
    x2, y2 = PinO(x2), PinO(y2)
    if x1 != ('1.' + '1' * (len(x1) - 2)):
        ed = '1.' + '0' * (len(x1) - 3) + '1'
        x1 = PinD(x1)
        ed = PinD(ed)
        x1 = plus(x1, '1.' + '0' * (len(x1) - 3) + '1')[2:]
        x1 = DinP(x1)
    else:
        x1 = '1.1' + '0' * (len(x1) - 2)

    print('Уменьшенный порядок: ', x1)
    print('Мантисса первого в мoк: ', x2[0] + x2)
    print('Мантисса второго в мoк: ', y2[0] + y2)
    print(' ', x2[0] + x2)
    print('+')
    print(' ', y2[0] + y2)
    s = plus(x2, y2)
    print('-------------')
    print(' ', s)

    if s[0] == '1':
        print('\n')
        print(' ', s[1:])
        print('+')
        print(' ', '00.' + '0' * (len(s[1:]) - 4) + '1')
        s = plus(s[2:], '0.' + '0' * (len(s[1:]) - 4) + '1')
        print('-------------')
        print(' ', s)
    s = s[:-1]
    return [s, x1]


def normal(x1, s):
    print('Необходима нормализация мантиссы сдвигом влево')
    s = s[:2] + s[3:] + '0'
    if x1 != ('1.' + '1' * (len(x1) - 2)):
        ed = '1.' + '0' * (len(x1) - 3) + '1'
        x1 = PinD(x1)
        ed = PinD(ed)
        x1 = plus(x1, ed)[2:]
        x1 = DinP(x1)
    else:
        x1 = '1.1' + '0' * (len(x1) - 2)
    print('Смещенная мантисса: ', s)
    print('Уменьшенный порядок: ', x1)
    return [x1, s]


def t_121(y1, y2, x2, s, zero, op):
    print('[mx]мдк + [-my]мдк = ', s[1:], end='\n')
    print('выполним суммирование с 1 пока разность не станет 0')
    while s != zero:
        s = s[2:]
        print(' ', s[0] + s)
        print('+')
        print(' ', '00.' + '0' * (len(s) - 3) + '1')

        s = plus(s, '0.' + '0' * (len(s) - 3) + '1')
        x2 = x2[:2] + '0' + x2[2:-1]

        print('-------------')
        print(' ', s)

    print('Смещенное первое [Mx\']пк = ', x2)
    if op == '-':
        y2 = str(1 ^ int(y2[0])) + y2[1:]
        print('[-My]пк = ', y2)

    x2, y2 = PinO(x2), PinO(y2)
    print('[Mx\']мок = ', x2[0] + x2)
    print('[My]мок = ', y2[0] + y2)
    print(' ', x2[0] + x2)
    print('+')
    print(' ', y2[0] + y2)
    s = plus(x2, y2)
    print('-------------')
    print(' ', s)

    if s[0] == '1':
        print('\n')
        print(' ', s[1:])
        print('+')
        print(' ', '00.' + '0' * (len(s[1:]) - 4) + '1')
        s = plus(s[2:], '0.' + '0' * (len(s[1:]) - 4) + '1')
        print('-------------')
        print(' ', s)

    if (s[1:3] == '01'):
        s, y1 = denormmin(y1, x2, y2)

    elif (s[1:3] == '10'):
        s, y1 = denormplu(y1, x2, y2)

    s = s[2:]

    print('сумма в обратном коде: ', s)
    print('сумма в прямом коде: ', PinO(s))
    s = PinO(s)
    if s[2] == '0':
        y1, s = normal(y1, s)

    print('Искомая сумма: ', y1 + '.' + s)


def t_122(x1, x2, y2, s, zero, op):
    print('[mx]мдк + [-my]мдк = ', s[0] + s, end='\n')
    print('выполним вычитание с 1 пока разность не станет 0')
    while s != zero:
        print(' ', s[0] + s)
        print('-')
        print(' ', '00.' + '0' * (len(s) - 3) + '1')
        for i in range(len(s) - 1, 1, -1):
            if s[i] == '1':
                c = i
                break
        s = s[:c] + '0' + '1' * (len(s) - c - 1)
        print('-------------')
        print(' ', s)

        y2 = y2[:2] + '0' + y2[2:-1]
    print('Смещенное второе [My\']пк = ', y2)

    if op == '-':
        y2 = str(1 ^ int(y2[0])) + y2[1:]
        print('[-My\'пк = ', y2)

    x2, y2 = PinO(x2), PinO(y2)
    print('[Mx]мок = ', x2[0] + x2)
    print('[-My\']мок = ', y2[0] + y2)
    print(' ', x2[0] + x2)
    print('+')
    print(' ', y2[0] + y2)
    s = plus(x2, y2)
    print('-------------')
    print(' ', s)

    if s[0] == '1':
        print('\n')
        print(' ', s[1:])
        print('+')
        print(' ', '00.' + '0' * (len(s[1:]) - 4) + '1')
        s = plus(s[2:], '0.' + '0' * (len(s[1:]) - 4) + '1')
        print('-------------')
        print(' ', s)

    if (s[1:3] == '01'):
        s, x1 = denormmin(x1, x2, y2)

    elif (s[1:3] == '10'):
        s, x1 = denormplu(x1, x2, y2)

    s = s[2:]
    print('сумма в обратном коде: ', s)
    print('сумма в прямом коде: ', PinO(s))
    s = PinO(s)

    if s[2] == '0':
        x1, s = normal(x1, s)

    print('Искомая сумма: ', x1 + '.' + s)


print('я умею складывать только числа одинаковой длины, надеюсь у вас они такие, если что допишите нули')
print('я надеюсь у всех числа заданы в ПК\n')

op = input('какая операция (+, -)\n')
x1, x2 = input('Машинное число первого\n'), input('Мантисса первого\n')
y1, y2 = input('Машинное число второго\n'), input('Мантисса второго\n')
print('\n\n')

y3 = str(1 ^ int(y1[0])) + y1[1:]
print('[-my]пк = ', y3)
x3, y3 = PinD(x1), PinD(y3)
print('[mx]мдк = ', x3[0] + x3)
print('[-my]мдк = ', y3[0] + y3)

print(' ', x3[0] + x3)
print('+')
print(' ', y3[0] + y3)
s = plus(x3, y3)
print('-------------')
print(' ', s)

if s[1:3] == '01':
    print('Положительное препеолнение -> искомая сумма равна первому числу: ', x1 + '.' + x2)
elif (s[1:3] == '10') or (s == '111.00'):
    if op == '+':
        print('Отрицательное препеолнение -> искомая сумма равна второму числу: ', y1 + '.' + y2)
    else:
        if y2[0] == '1':
            print('Отрицательное препеолнение -> искомая сумма равна второму числу со знаком минус: ',
                  y1 + '.' + '0' + y2[1:])
        else:
            print('Отрицательное препеолнение -> искомая сумма равна второму числу со знаком минус: ',
                  y1 + '.' + '1' + y2[1:])
elif s[1:3] == '11':
    print('\n\n')
    print('mx < my')
    t_121(y1, y2, x2, s, '100.' + '0' * (len(y1) - 2), op)
else:
    print('\n\n')
    print('mx > my')
    t_122(x1, x2, y2, s[2:], '0.' + '0' * (len(y1) - 2), op)

