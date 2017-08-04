#Example1: x = 123, return 321
#Example2: x = -123, return -321

# for i in str(x):
#     li.insert(0,i)

#翻转数字基础版

def reverseInteger(x):
    li = []

    ll = [li.insert(0, i) for i in str(x)]

    z = "".join(li)

    return int(z)

print (reverseInteger(345))

#翻转数字升级版

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            r = int(str(x)[::-1])

        else:
            x = abs(x)
            z = -1
            r = int(str(x)[::-1]) * z

        return r * (-2 ** 31<r < 2 ** 31)

so = Solution()
print (so.reverse(-567))




