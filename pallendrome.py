word=input("type in a word and I will tell you if it is a pallendrome ")
ltrs=[*word]
# print(ltrs)
num=len(ltrs)

if num%2==1 and num>=3:
    mid=num/2
else:
    # mid=num/2
    # mid=mid-1
    print("the word " + word + " is not a pallendrome")
    quit()
mid=int(mid)
x=0
pallendrome=True
while(mid-x!=-1):
    if(ltrs[mid+x]==ltrs[mid-x]):
        x=x+1
    else:
        pallendrome=False
        break
# print(pallendrome)
if pallendrome==True:
    print("the word \"" + word + "\" is a pallendrome")
else:
    print("the word \"" + word + "\" is not a pallendrome")