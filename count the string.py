string=str(input("enter the string"))
freq={}
for s in string:
    if s in freq:
        freq[s]=+1
    else:
        freq[s]=1
print(freq) 