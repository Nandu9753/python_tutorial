str = "aaabcadea"
count = 0
for i in range(0,len(str)-1):
    if(str[i]!=str[i+1]):
        count +=1
print(count)        