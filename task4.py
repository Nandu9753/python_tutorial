def lst_merge(l1,l2):
    lst = []
    length = min(len(l1),len(l2))
    index = 0
    for i in range(length):
        lst.append(l1[i])
        lst.append(l2[i])
        index += 1
    if(len(l1) > len(l2)):
        lst.extend(l1[index:])    
    if(len(l1) < len(l2)):
        lst.extend(l2[index:])   
    return lst 
l1 =[1,3,7,8,9]
l2=[2,4,6,6,8,3]        
print(lst_merge(l1,l2))    