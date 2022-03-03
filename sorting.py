arr=[5,2,8,7,1,56,78,0,5,6,46,549,6,235,164];
p=0;

print("elemts of original array:");
for i in range(0,len(arr)):
    print(arr[i],end="");

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            p=arr[i];
            arr[i]=arr[j];
            arr[j]=p;    
print();
print("elements of array sorted in ascending order :");
for i in range(0,len(arr)):
    print(arr[i],end=" ");