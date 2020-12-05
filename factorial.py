def factorial(x):
   if x==1:
    return 1
   else:
    return x*factorial(x-1)
f=factorial(9)
print("factorial of 9 is",f)
