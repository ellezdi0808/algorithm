list1 = [2,5,8,11]
list12 = [1,3,7,8,17,19]

def merge_sort(l1,l2):

    temp = []

    while len(l1)>0 and len(l2)>0:
        if l1[0]<l2[0]:
            temp.append(l1[0])
            l1.remove(l1[0])

        else:
            temp.append(l2[0])
            l2.remove(l2[0])

    temp.extend(l1)
    temp.extend(l2)

    return set(temp)


print (merge_sort(list1,list12))