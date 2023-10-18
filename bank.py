def main():
    v = str(input("Приветствие: "))
    if v == "здравствуйте":
        print ('$0')
    else:
        v = v[0]
        if v == 'з':
            print ('$20')
        else:
            print ('$100')


main()