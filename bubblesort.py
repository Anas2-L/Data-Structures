def bubblesort(list1):
    n=len(list1)
    for i in range(n-1):
        for j in range(0,n-1-i):
            if(list1[j]>list1[j+1]):
                list1[j],list1[j+1]=list1[j+1],list1[j]
    
    print(list1)

list1=[]
print("Enter 5 numbers\n")
for i in range(5):
    x=int(input())
    list1.append(x)
print(list1)
bubblesort(list1)