def testing(s):
    cSet = set()
    start = 0
    lss = 0
    for end in range(len(s)):
        if s[end] in cSet: 
            while s[end] in cSet:
                cSet.discard(s[start])
                start+=1


        if s[end] not in cSet:
            cSet.add(s[end])
            lss =max(lss,len(cSet))
    return cSet
print(testing("abacadefea"))