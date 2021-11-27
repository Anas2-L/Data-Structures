def binarysearch(list1,num):
    first=0
    last=len(list1)-1
    resultindex=-1
    while((first<=last) and (resultindex==-1)):
        mid=(first+last)//2
        if(list1[mid]==num):
            resultindex=mid
        else:
            if(num>list1[mid]):
                first=mid+1
            else:
                last=mid-1

    return resultindex
list1=[5,10,15,20,35,67,77]
print("Number is found at position ",binarysearch(list1,10))    



