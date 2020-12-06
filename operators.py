

class Num:
    def __init__(self, value):        
        self.var = 10
        if type(value) == type(10):
            self.var = value
            
    def __str__(self):
        return str(self.var)
        
    def __add__(self, other):
        return Num(self.var + other.var)
    
    def __mul__(self, other):
        return Num(self.var * other.var)    
    def __mod__(self, other):
        return Num(self.var % other.var)
    def __lt__(self, other):
        if(self.var < other.var): 
            return "var2 is lessthan var1"
        else: 
            return "var1 is less than var2" 
    def __eq__(self, other): 
        if(self.var == other.var): 
            return "Both are equal"
        else: 
            return "Not equal"
var1 = Num(25)
var2 = Num('some sting here')

var3 = var1 + var2
var4 = var1 * var2
var5 = var1 % var2

print(f'var1--> {var1}')
print(f'var2--> {var2}')
print(f'var3--> {var3}')
print(f'var4--> {var4}')
print(f'var5--> {var5}')
print(var2 < var1)
print(var1==var2)