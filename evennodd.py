number = int(input("enter a number:"))
even = False
odd = False

num = number
if num > 0 :
    if(num % 2) == 0:
        even = True
    else :
        odd = True

if even == True:
    oddcount = 0
    evencount = 0
    num = number
    while evencount < 5 :
        if(num % 2) == 0:
            print(num)
            evencount = evencount + 1
            num = num + 1
        else:
            num = num + 1
            
    num = number
    while oddcount < 5 :
        if(num % 2) != 0:
            print(num)
            oddcount = oddcount + 1
            num = num + 1
        else:
            num = num  + 1
            
if odd == True:
    evencount = 0
    oddcount = 0
    num = number
    while oddcount < 5 :
        if(num % 2) != 0:
            print(num)
            oddcount = oddcount + 1
            num = num + 1
        else:
            num = num  + 1
            
    num = number
    while evencount < 5 :
        if(num % 2) == 0:
            print(num)
            evencount = evencount + 1
            num = num + 1
        else:
            num = num + 1