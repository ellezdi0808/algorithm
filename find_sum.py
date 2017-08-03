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

######################


nums = [9,3,5,8,2,7,11,15]
target = 20
class Solution:
    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    print("({},{})".format(i, j))
                    temp.append(i)
                    temp.append(j)
                else:
                    continue

        return temp

so = Solution()

print (so.twoSum(nums,target))

######################


lists = [9,3,5,8,2,7,11,15]
target = 20


class Solution:
    def twoSum(self, lists, target):
        if len(lists) <= 1:
            return False
        buff_dict = {}
        for i in range(len(lists)):
            if lists[i] in buff_dict:
                return [buff_dict[lists[i]], i]
            else:
                buff_dict[target - lists[i]] = i

so = Solution()
print (so.twoSum(lists,target))







