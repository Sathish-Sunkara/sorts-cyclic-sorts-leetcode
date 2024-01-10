"""
arrra as [1,n]
but one number is missing find that one
https://leetcode.com/problems/missing-number/
"""
def cyclic(array) :
    n = len(array)
    # sort in cyclic sort manner
    i = 0 
    while i <= n-1 :
        correct = array[i] - 1
        
        if correct < n or array[i] > 0 or array[i] != array[correct]  :
            temp =  array[i] 
            array[i] =  array[correct]
            array[correct] = temp
        else :
            i += 1
    return array

def missing(arr):
    n = len(arr)
    arr = cyclic(arr)
     # print(arr)
    for i , ch in enumerate(arr) :
        if i != ch :
            return i
    return n
        

ar = [9,6,4,2,3,5,7,0,1]  
print(missing(ar))
        
    
