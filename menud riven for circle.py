def circle():
    print ("choose circle")
    radius=int(input("enter radius\n"))
    print("area of circle",3.14*(radius**2),"square units.")

def square():
    print("choose square")    
    side=int(input("enter size of side of square\n"))
    print("area of square ",side**2,"square units.")
    
def rectangle():
    print("choose rectangle")
    length=int(input("enter the length of rectangle :"))
    breadth=int(input("enter the breadth of rectangle :"))
    print("area of rectangle ",length*breadth,"square units.")

print("menu -\n"
      "1.circle\n"
      "2.square\n"
      "3.rectangle\n")        
      
x=int(input("select the shape"))

if x==1:
    circle()      
elif x==2:
    square()  
elif x==3:
    rectangle()
else :
    print("invalid input")          