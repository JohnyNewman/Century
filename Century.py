def century(year):
    year = str(year)
    if len(year) == 2:
        return(1)
    else:
        ldig = year[-2:]
        dig = year[:-2]
        result = int(ldig[0]) + int(ldig[1])
        if result > 0:
            return(int(dig) + 1)
        else:
            return(int(dig))