A = [i for i in range(1,100)]
B = [i for i in range(1,100)]

# there are multiple solutions for X = A[i] + B[j]
# Each solution set has multiple 

# X = A[i] + B[j]
# Y = A[i] * B[j]
# 找到X 和 Y的唯一相同解

X = [i for i in range(2,199)] # 和的范围是2到198
Y = []
for x in A:
    for y in B:
        Y.append(x*y)
Y = set(Y)
Y = list(Y)
Y.sort()

# 首先Y不能有质数
def prime_check(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True # number 是质数

def multiple_product(number):
    set1 = set()
    list1 = list()
    for i in range(2,number):
        if number % i == 0:
            if i <= 99 and number %i <= 99:
                if i not in set1:
                    list1.append((i,number//i))
                set1.add(i)
                set1.add(number//i)
                
    if len(set1) > 2:
        return list1
    else: return False

        
def multiple_sum(number):
    set1 = set()
    list1 = list()
    for i in range(1,100):
        if 1 <= number - i <= 99:
            if i not in set1:
                list1.append((i,number-i))
            set1.add(i)
            set1.add(number-i)

    if len(set1) > 2:
        return list1
    else: return False

Y.remove(1)
Y.remove(2)
Y.remove(3)
X.remove(2)
X.remove(3)
X.remove(198)
X.remove(197)

big_list_product = []
big_list_sum = []


for i in range(len(Y)):
    check = multiple_product(Y[i])
    if check is False:
        Y[i] = 0
    else:
        big_list_product.append(check)

while Y.count(0):
    Y.remove(0)

for i in range(len(X)):
    check = multiple_sum(X[i])
    if check is False:
        X[i]= 0
    else:
        big_list_sum.append(check)
while X.count(0):
    X.remove(0)
    
final_list =[]    
    
    
flag = True
for temp_list in big_list_sum:
    for combination in temp_list:
        if combination[0] * combination[1] not in Y:
            flag = False
            break
    if flag is False:
        flag = True
        continue
    elif flag is True:
        final_list.append(temp_list)

final_sum = []
for i in range(len(final_list)):
    final_sum.append(sum(final_list[i][0]))


small_list_product = []
for temp_list in big_list_product:
    if len(temp_list) <= 2:
        flag = True
        for i in temp_list:
            if i[0] > 99 or i[1] > 99:
                flag = False
                break
        if flag is True:
            small_list_product.append(temp_list)

for temp_list in final_list:
    for temp_tuple in temp_list:
        for product_list in small_list_product:
            if temp_tuple in product_list:
                print(temp_tuple)