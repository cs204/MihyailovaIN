import re
def main():
    v = input("Верблюжий стиль: ")

    s = re.sub( r"([A-Z])", r" \1", v).split()
    res = ''
    for x in s:
        res += x+'_'

    print(res.rstrip("_").lower())


main()