


def leftBelowMultiplication():#左下三角形

    for i in range(1,10):
        for j in range(1,i+1):
            k = i*j
            print ("{}*{}={}".format(i,j,k),end="  ")
        print ("")


def leftUpMultiplication(): #左上三角形

    for i in range(1,10):
        for j in range(i,10):
            k = i*j
            print ("{}*{}={}".format(i,j,k),end="  ")
        print ("")


leftUpMultiplication()
