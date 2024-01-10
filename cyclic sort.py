def cyclic(array) :
    n = len(array)
    # sort in cyclic sort manner
    i = 0 
    while i <= n-1 :
        correct = array[i] - 1
        if correct >= n :
            i += 1
            continue
        if array[i] != array[correct] :
            temp =  array[i] 
            array[i] =  array[correct]
            array[correct] = temp
        else :
            i += 1
    return array


arr = [1,4,2,5]
print(cyclic(arr))