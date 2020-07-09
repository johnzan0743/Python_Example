"""
取整数的每个数位
"""

for i in range(10,100000):
    single = i % 10
    ten = i //10*1 %10
    hundred = i //10**2 %10
    thousand = i //10**3 %10
    ten_thousand = i //10**4 %10
    for _ in range(1,6):
        if i //10**_ == 0:
            break
    if single**_ + ten**_ + hundred**_ + thousand**_ +\
    ten_thousand**_ == i:
            print(i)


"""
求正整数的反向数字
"""
num = int(input ('Please input a number: '))

i = 0
reverse_number = 0
while num // 10**i > 0:
    i +=1

num_of_digit = i #正常的几位数
for _ in range(num_of_digit):
    single_digit = num // 10**_ %10
    reverse_number += single_digit* 10**(num_of_digit-_-1)


"""
百钱买百鸡
公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡
"""
for x in range(100):
    for y in range(100):
        z = 100 - x - y
        if 5*x + 3*y + z/3 == 100:
            print(f'There are {x} roosters, {y} hens and {z} chicks')


"""
斐波那契数列
"""
n = int(input('Please input the number of Fibo List: '))
Fibo_list = [1,1]
for i in range (1,n-1):
    Fibo_list.append(Fibo_list[i]+Fibo_list[i-1])

print(Fibo_list)

"""
找出10000以内的**完美数**。

   > **说明**：完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。
"""


for i in range(2,10001):
    true_factor=0
    for j in range(2,i+1):
        if (i/j).is_integer() == True:
            true_factor +=(i/j)
    if true_factor == i:
        print(i,end=' ')

"""
输出**100以内所有的素数**。

> **说明**：素数指的是只能被1和自身整除的正整数（不包括1）。
"""

list =[]
for i in range (2,100):
    list.append(i)

for i in range(2,100):
    for j in range(2,i+1):
#        if j != i and (i/j).is_integer() == True:
        if i != j and (i%j) == 0:
            list.remove(i)
            break

print(list)



            




