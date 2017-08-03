# 删除一个字符串中连续超过一次的空格


def  del_space(str):
    split_str = str.split(" ")
    str_list = [i for i in split_str if i != ""]
    result_str = " ".join(str_list)
    return result_str


str = "welcome  ,  to   alisa         home"

print (del_space(str))

