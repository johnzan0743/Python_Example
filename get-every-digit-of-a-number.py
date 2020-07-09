class Solution:
    def getEachDigitNumber(self,num):
        digit_list = []
        while num > 0:
            digit = num % 10
            digit_list.append(digit)
            num = num // 10
        return digit_list
            
num = 514      
A = Solution()
List = A.getEachDigitNumber(num)