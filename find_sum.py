listvalue = [2,4,6,1,8,10,17,9,19]
n = 18

listnnn = []
def sum_element(li,n):
    for i in range(0,len(listvalue)):
        for j in range(i+1,len(listvalue)):
            if listvalue[i] + listvalue[j] == n:
                print ("{}+{}={}".format(listvalue[i],listvalue[j],n))
                listnnn.append("({},{})".format(i,j))

            else:
                print (i,j)
                continue
    if listnnn:
        return listnnn
    else:
        return "没有找到两个元素相加和为目标数"

print (sum_element(listvalue,n))
