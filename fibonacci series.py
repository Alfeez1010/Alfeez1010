n_terms=int(input("how many terms print.? \n"))

n1=0
n2=1
count=0

if n_terms<=0:
    print("enter the positive integer")
    
elif n_terms == 1 :
    print("the fibonacci series is", n_terms , " ")
    print(n1)
  
else:
    print("the fibonacci sequence is ")
    while count<n_terms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1    
        