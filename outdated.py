def main():

    bl={
        "январь": "01",
        "февраль": "02",
        "март": "03",
        "апрель": "04",
        "май": "05",
        "июнь": "06",
        "июль": "07",
        "август": "08",
        "сентябрь": "09",
        "октябрь": "10",
        "ноябрь": "11",
        "декабрь": "12",
    }


    while True:

        dat_t = input("Дата: ")
        dat = dat_t.split()
        if len(dat) == 1:
            dat = dat_t.split(".")
        
        try:
            d = int(dat[0])
            m = int(dat[1])
            y = int(dat[2])
            if (m > 0) and (m < 13) and (d > 0) and (d < 31) :
                print(str(y)+"-"+str(f"{m:02}")+"-"+str(f"{d:02}"))
                break
        except ValueError:
            pass
        try:
            d = int(dat[0])
            m = str(dat[1])
            y = int(dat[2])
            print(str(y)+"-"+bl[m]+"-"+str(f"{d:02}"))
            break
        except ValueError:
            pass


main()