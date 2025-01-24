arr1=list(map(int,input("enter the list values:").split()))
arr2=list(map(int,input("enter the list values:").split()))

intersection = []

for num in arr1:
    if num in arr2 and num not in intersection: 
        intersection.append(num)
print(intersection)