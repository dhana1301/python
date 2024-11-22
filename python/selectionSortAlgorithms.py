def selection_sort(arr):
    n = len(arr) 
    for i in range(n-1):

        min_index = i 
        for j in range(i+1,n):
            
            if(arr[j] < arr[min_index]):
                min_index = j 
             
        arr[i],arr[min_index] = arr[min_index],arr[i]



array = [65,78,84,12,17] 
selection_sort(array)

print("sorted array:" ,array)