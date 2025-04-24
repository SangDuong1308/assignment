# pseudo-code:
# Initialize max_current = a[0]
# Initialize max_global = a[0]

# For i: 1 -> N-1:
#     max_current = max(a[i], max_current + a[i])
#     max_global = max(max_global, max_current)

# Return max_global

def find_max_subarray_sum(arr):
    if not arr:
        return 0
    
    max_current = result =  arr[0]
    
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        result = max(result, max_current)
    
    return result

if __name__ == "__main__":
    arr1 = [-2, 1, -3, 4, -1, -2, -1, -5, -4]
    arr2 = [-5, -5, -5, -5]
    arr3 = [100, -100, 100, -100, 100]
    print(find_max_subarray_sum(arr1))
    print(find_max_subarray_sum(arr2))
    print(find_max_subarray_sum(arr3))