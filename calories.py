def main():
    v = input("Фрукт: ")

    fructs = [['Apple', 130], ['Avacado', 50], ['Lime', 20]]
    for m in fructs:
        if m[0] == v:
            print('Калории: '+str(m[1]))


main()