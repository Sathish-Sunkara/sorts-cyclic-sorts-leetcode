def bubble(arr):
    n = len(arr)
    for i in range(0,n) :
        swapped = False
        for j in range(0,n-1-i) :
            if arr[j] > arr[j+1] :
                arr[j] , arr[j+1] = arr[j+1] , arr[j] 
                swapped = True
        if not swapped :   # optimality code
            break
    return arr

arr = [2,4,3,5,1]
print(bubble(arr))