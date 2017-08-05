#冒泡排序原理: 每一趟只能将一个数归位, 如果有n个数进行排序,只需将n-1个数归位, 也就是说要进行n-1趟操作(已经归位的数不用再比较)
#冒泡排序的思想: 每次比较两个相邻的元素, 如果他们的顺序错误就把他们交换位置
#比较len-1回，，每回从第一数比较到比上一次少一个元素，也就是每一趟都要比较两个相邻的数



listStart = [12, 35, 99, 18, 76,11,3,679,70]


def bubbleSort(list):
    for j in range(len(listStart)-1):
        for i in range(len(listStart)-j-1):
            if listStart[i]<listStart[i+1]:
                listStart[i],listStart[i+1] =listStart[i+1],listStart[i]
            else:
                continue

    return (listStart)

print (bubbleSort(listStart))