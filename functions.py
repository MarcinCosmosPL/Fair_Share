from Communicators import *

def MoneyFormat(absAmount): #converts amount in lowest money units (gr = 0.01 pln) to string in zl,gr form
    if len(str(absAmount))==1:
        return "0,0"+str(absAmount)
    elif len(str(absAmount))==2:
        return "0,"+str(absAmount)
    else:
        return str(absAmount)[:-2]+","+str(absAmount)[-2:]

def fairDivider(cost, FandC): #main function - takes the cost and list of friends and contributions - return text of fare-share result
    #the cost in FandC must be in their lowest units (gr = 0.01 pln) - therefore we later use moneyformat
    #needs MoneyFormat function
    result = ''
    rest = 0
    divider = len(FandC)  # how many people to divide

    if cost % len(FandC) != 0:  # the case when cost is not divided - get the rest
        while cost % len(FandC) != 0:
            cost -= 1
            rest += 1
        result += restWarning + str(MoneyFormat(rest)) + '\n'

    share = int(cost / len(FandC))
    result += shareText+str(MoneyFormat(share)) + '\n'

    for friend in FandC:
        if friend[1] < share:
            result += toPay.format(friend[0], MoneyFormat(share - friend[1]))
        elif friend[1] > share:
            result += toReceive.format(friend[0], MoneyFormat(friend[1] - share))
        else:
            result += isOK.format(friend[0])

        if friend[1] > 0:
            result += ' ' + hasPaid.format(MoneyFormat(friend[1]))+'\n'
        else:
            result += '\n'

    return result

def grFormat(zl,gr): #combines two numeric strings and return them as integer
    return int(zl+gr)

def FandCDisplayer(FandClist):
    result = ''
    for FandC in FandClist:
        result+= personHasPaid.format(FandC[0],MoneyFormat(FandC[1]))+"\n"
    return result


# Testing
#print(fairDivider(1500, [("Paul", 500), ("Robert", 500), ("Artur", 600)]))
#print(MoneyFormat(grFormat("19", "00")))
#print(FandCDisplayer([("Paul", 500), ("Robert", 500), ("Artur", 600)]))