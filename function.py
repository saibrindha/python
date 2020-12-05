
def recur(num):
 if num<=10: 
  print(f'{num} ',end='')
  recur(num+1)
recur(1)