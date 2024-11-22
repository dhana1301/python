def binary_search(arr,target):
    first_index = 0 
    last_index = len(arr) - 1 

    while first_index <= last_index: 
        mid_index = (first_index + last_index) // 2 

        if (arr[mid_index] == target):
            return mid_index 
        elif(arr[mid_index] < target):
            first_index = mid_index + 1 
        else :
            last_index = mid_index -1  
    
    return -1



sorted_arr = [1,2,3,4,5,6,7] 
target = 6 
result = binary_search(sorted_arr,target) 

if (result != -1):
    print(f"Target element found at index {result}") 
else :
    print("Target elemnet not found")