year = int(input())
thou = (year // 1000) % 10
hun = (year // 100) % 10
ten = (year // 10) % 10
unit = (year // 1) % 10

for hun_thou in range(0 , 10):
    for thousnt in range(0, 10):
        for hundrds in range(0, 10):
            for tents in range(0, 10):
                for units in range(0, 10):
                    new_year = hun_thou * 10000 + thousnt * 1000 + hundrds * 100 + tents * 10 + units
                    if hundrds != units and hundrds != tents and tents != units and thousnt != hundrds and thousnt != tents \
                        and thousnt != units and year < new_year:
                            print(new_year)
                            exit()




#and units != unit


