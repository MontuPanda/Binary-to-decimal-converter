binary=[]
inp=input("Enter binary:")
binary[:0]=inp
dec=0
length=len(binary)-1
counter=0
while length>-1:
    x=int(binary[counter])
    ans=x*2**length
    dec=dec+ans
    length=length-1
    counter=counter+1
print(dec)