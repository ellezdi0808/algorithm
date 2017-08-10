# 题目，给你一个列表，删除2 前面是0 的那个0

a = [1, 1, 0, 2, 0, 0, 8, 3, 0, 2, 5, 0, 2, 6]

# 机智的办法
[x[0] for x in zip(a,a[1:]+[None]) if x!=(0,2)]


def delete_element():
    delete_list = []
    for i,item in enumerate(a):
        if item ==2:
            if a[i-1]==0:
                delete_list.append(i-1)

    return [item for i,item in enumerate(a) if i not in delete_list]

print (delete_element())
