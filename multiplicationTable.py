


def leftBelowMultiplication():#左下三角形

    for i in range(1,10):
        for j in range(1,i+1):
            k = i*j
            print ("{}*{}={:>2}".format(i,j,k),end="  ")
        print ("")


def leftUpMultiplication(): #左上三角形

    for i in range(1,10):
        for j in range(i,10):
            k = i*j
            print ("{}*{}={:>2}".format(i,j,k),end=" ")
        print ("")


def RightUpMultiplication(): #右上三角形

    for i in range(1,10):
        for k in range(1,i):
            print (end=" "*7)
        for j in range(i,10):
            k = i*j
            print ("{}*{}={:>2}".format(i,j,k),end=" ")
        print ("")


def RightDownMultiplication():# 右下三角形
    for i in range(1,10):
        for k in range(1,10-i):
            print (end=" "*7)
        for j in range(1,i+1):
            print ("{}*{}={:>2}".format(i,j,i*j),end=" ")
        print (" ")


RightDownMultiplication()
