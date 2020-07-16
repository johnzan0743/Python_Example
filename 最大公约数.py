def hcf(x,y):
    min_value = min(x,y)

    for i in range(2,min_value+1):
        if x%i == 0 and y%i == 0:
            hcf_1 = i   # i是在更新中的，只要满足条件，就会更新一次，最后会产生最大的i
    
    return hcf_1