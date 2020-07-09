mylist = [20,50,22,-22,0,15,222,28,29,99,1999,100823,55,35,5,1,2,3,8,9,55,10239,234234]
def lgfind(arr,v):    
    arr = sorted(arr)#排序数组，从小到大
    print(arr)    
    start = 0 #变量开始
    arrLen = len(arr)-1 #变量结束 
    while( start <= arrLen ):       
        mid = (start + arrLen) // 2 #变量中间值  
        print('mid',mid)        
        #如果中间的找到直接返回
        if arr[mid] == v:
            return v        
        #比对大小，看看我们要的结果是在上半段，还是下半段
        if arr[mid] > v:
            arrLen= mid - 1 #结果在上半段
        else:
            start= mid + 1 #结果在下半段 
 
    return false #没有则返回假
    
have = lgfind(mylist,28)
print(have)