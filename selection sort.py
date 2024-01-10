def selection(array):
    n = len(array)
    for i in range(n):
        for j in range(i+1 , n):
            if array[i] > array[j] :
                array[i] , array[j] = array[j] , array[i]  # swaping
    return array


array = [3,2,4,5,1]
print(selection(array))
