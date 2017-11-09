l = [3,5,23,44,56,2,5,8,54,678,875]

def sort_list():
    one = l[0]
    two = l[0]
    for i in range(1,len(l)):
        if l[i]>one:
            two = one
            one = l[i]
        elif l[i]>two:
            two = l[i]
        else:
            pass
    print ("second number is {}".format(two))


sort_list()
