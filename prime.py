num = int(input("Enter a number : "))  
count = 0 
  
while count < 100:
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                num = num + 1
                break
            else:
                count = count + 1
                print(num )
                num = num + 1
                break