import keyboard

def main():

    bl={
        "кофе": 20.00,
        "чай": 10.00,
        "булочка": 5.00,
        "салат": 30.40,
        "пирожное": 45.50
    }
    res = 0
    while True:
        try:
            x = get_float(bl)

            res += x

        except EOFError:
            print("\nСумма: "+str('%.2f' % res))
            break


def get_float(x):
    while True:
        try:
            return float(x[""+input("Блюдо: ")+""])
        except ValueError:
            pass

main()