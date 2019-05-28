def Median(arr1,arr2):
     arr1.extend(arr2)
     arr1.sort()
     if len(arr1)%2==0:
         return (arr1[int(len(arr1)/2)]+arr1[int(len(arr1)/2)-1])/2
     else:
         return arr1[int(len(arr1)/2)]




a=[1,2,8,9,10,11,12]
b=[3,4,5,6,7]
print(Median(a,b));