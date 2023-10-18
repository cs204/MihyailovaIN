def main():

    print('Нужная сумма: 50')
    v = 50
    while v > 0:

        temp = int(input('Вставьте монету: '))
        if temp == 50:
            v = v-temp
            if v > 0:
                print('Нужная сумма: ' + str(v))
                continue
            else:
                continue

        elif temp == 20:
            v = v-temp
            if v > 0:
                print('Нужная сумма: ' + str(v))
                continue
            else:
                continue
        elif temp == 10:
            v = v-temp
            if v > 0:
                print('Нужная сумма: ' + str(v))
                continue
            else:
                continue
        elif temp == 5:
            v = v-temp
            if v > 0:
                print('Нужная сумма: ' + str(v))
                continue
            else:
                continue

        print('Нужная сумма: ' + str(v))

    print('Ваша сдача: ' + str(abs(v)))



main()