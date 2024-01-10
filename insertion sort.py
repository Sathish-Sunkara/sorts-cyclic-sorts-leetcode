def insert(arr , ele) :
    n = len(arr)
    j = n - 1
    while j >= 0 and arr[j] > ele :
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = ele
    return arr

def insertion(arr) :
    
    n = len(arr)
    for i in range(1,n) :
        counter = i
        while (arr[counter] < arr[counter-1] and counter >= 1) :
            arr[counter] , arr[counter-1] = arr[counter-1] , arr[counter]
            counter -= 1
    return arr



arr = [7,3,2,5,4,6,1]
ele = 4
print(insertion(arr))