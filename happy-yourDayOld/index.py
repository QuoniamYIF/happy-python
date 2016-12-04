def nextDay(year, month, day):
    """ Comment """
    if day < 30:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

print nextDay(1994, 12, 10)