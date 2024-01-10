# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
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

def missing_numbers(arr) :
    n = len(arr)
    arr = cyclic(arr)
     # print(arr)

    l = []
    for i , ch in enumerate(arr) :
        if i+1 != ch :
            l.append(i+1)
    return l

ar = [1,1,3,3,5,5,7,9,9]  
print(missing_numbers(ar))
        
        