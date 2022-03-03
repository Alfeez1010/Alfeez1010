from select import select


def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q

print("select a operation")
print("a.add")
print("b.subtract")
print("c.multiply")
print("d.divide")

select=input("select the (a,b,c,d)")

num1=int(input("enter 1st number\n"))
num2=int(input("enter 2nd number\n"))

if select=="a":
     print(num1,"+",num2,"=",add(num1,num2))

elif select=='b':
    print(num1,"-",num2, "=",sub(num1,num2))
    
elif select=='c':
    print(num1, "*",num2,"=",multiply(num1,num2))
    
elif select=='d':
    print(num1 , "/", num2, "=", divide(num1,num2))
    
else :
    print("invalid input")            