units = ["","one","two","three","four","five","six","seven","eight","nine","ten",
     "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

decimals = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def findLength(n):
    n += 1
    letters = 0
    for i in range(n):
        num = makeNumber(i)
        letters += len(num)
    print(letters)

def makeNumber(n):
    if n < len(units):
        return units[n]
    elif n < 100:
        return decimals[int(n/10)-2] + units[n%10]
    elif n < 1000:
        num = units[int(n/100)] + "hundred"
        if n%100 != 0:
            num += "and" + makeNumber(n%100)
        return num
    elif n == 1000:
        return "onethousand"
    
