class Solution:
    def bubble(self,bubbleList):
        listLength = len(bubbleList)
        while listLength > 0:
            for i in range(listLength - 1):
                if bubbleList[i] > bubbleList[i+1]:
                    bubbleList[i], bubbleList[i+1] = bubbleList[i+1], bubbleList[i]
            listLength -= 1
            print(bubbleList)

            
bubbleList = [8,100,2,3,1,0,-10]

# nums = [1,0,-1,0,-2,2]
# target = 0
A = Solution()
B = A.bubble(bubbleList)
'''
冒泡算法的核心是每一步都把当前list中最大的数字排到最后
然后把需要处理的数组的最后一位甩掉，再继续排序
'''