def main():
    v = str(input("Дробь: "))
    temp = v.split("/")


    for t in temp:
        if not t.isdigit():
            v = str(input("Дробь: "))
            temp = v.split("/")
            break

    try:
        x = int(temp[0])
        y = int(temp[1])
        res = x/y
        res = int(res*100)
        if res > 98:
            print('F')
        elif (res > 1) and (res < 99):
            print(str(res)+'%')
        if res < 2:
            print('E')




    except ValueError:
        f = 3
        # v = str(input("Дробь: "))
        # temp = v.split("/")

        # for t in temp:
        #     if not t.isdigit():
        #         v = str(input("Дробь: "))
        # x = int(temp[0])
        # y = int(temp[1])
        # res = x/y
        # res = int(res*100)
        # if res > 98:
        #     print('F')
        # elif (res > 1) and (res < 99):
        #     print(str(res)+'%')
        # if res < 2:
        #     print('E')

    except ZeroDivisionError:
        v = str(input("Дробь: "))
        temp = v.split("/")

        for t in temp:
            if not t.isdigit():
                v = str(input("Дробь: "))
        x = int(temp[0])
        y = int(temp[1])
        res = x/y
        res = int(res*100)
        if res > 98:
            print('F')
        elif (res > 1) and (res < 99):
            print(str(res)+'%')
        if res < 2:
            print('E')





main()