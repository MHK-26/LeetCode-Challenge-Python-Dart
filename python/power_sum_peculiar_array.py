def powerSumPeculiarArray(array,power=1):
    sum = 0
    for i in array:
        if type(i) ==list:
            sum += powerSumPeculiarArray(i,power+1)
        else:
            sum += i
    
    return sum**power



print(powerSumPeculiarArray([1,2,[3,4],[[2]]]))