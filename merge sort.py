def merge(arr):
    if len(arr) == 1 :
        return arr
    if len(arr) == 2 :
        if arr[0] > arr[1]:
            arr[0] , arr[1] = arr[1] , arr[0]
            return arr
        else :
            return arr
    l = 0
    r = len(arr) - 1
    mid = (l+r)//2  # split the array

    # recursively split the array at edge recuse base cases are returnes means small sorted array parts (first , second parts) are returned
    first = merge(arr[:mid])
    second = merge(arr[mid:])

    i = 0 ; j = 0 ; k = 0
    while i < len(first) and j < len(second)  :
        if first[i] < second[j] :
            arr[k] = first[i]
            i += 1 
        else :
            arr[k] = second[j]
            j += 1
        k += 1
    while i < len(first) :
        arr[k] = first[i]
        k += 1
        i += 1

    while j < len(second) :
        arr[k] = second[j]
        k += 1
        j += 1

    return arr




arr = [6,4,7,2,9,3,1,6,4,8,9,3]
print(merge(arr))