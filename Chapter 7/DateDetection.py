date = input('Enter date in DD/MM/YYYY format : ')
def checkdate(date):
    l = date.split('/')
    leapyear = 0
    while True:
        #Check if year is valid
        if int(l[2]) < 1000 or int(l[2]) > 2999 :
            return False
            break

        #Check if it is a leap year 
        if int(l[2]) % 4 == 0 :
            leapyear = 1

        #Check if the month is valid 
        if int(l[1]) > 12 or int(l[1]) < 1 :
            return False
            break

        #Check if the date is correct
        if int(l[1]) in [1.3,5,7,8,10,12]:
            if int(l[0]) < 1 or int(l[0]) > 31 :
                return False
                break
        if int(l[1]) in [4,6,9,11]:
            if int(l[0]) < 1 or int(l[0]) > 30 :
                return False
                break
        if int(l[1]) == 2 :
            if leapyear == 1 :
                if int(l[0]) < 1 or int(l[0]) > 29 :
                    return False
                    break
            else:
                if int(l[0]) < 1 or int(l[0]) > 28 :
                    return False
                    break
        #if everything is in order
        return True

print(checkdate(date))