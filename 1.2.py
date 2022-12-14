def find_sorting_window(nums):
    n = len(nums)
    i = 0

    # Get indexes of elements that are out of order
    out_of_order_indexes = []
    high = nums[0]
    for i in range(n):
        if nums[i] < high: 
            out_of_order_indexes.append(i)
        else:
            high = nums[i]
    if len(out_of_order_indexes) == 0:
        return None

    # Get min and max elements out of order
    minIndex = out_of_order_indexes[0]
    maxIndex = out_of_order_indexes[0]
    minVal = nums[minIndex]
    maxVal = nums[maxIndex]
    for index in out_of_order_indexes:
        if nums[index] < minVal:
            minVal = nums[index]
            minIndex = index
        if nums[index] > maxVal:
            maxVal = nums[index]
            maxIndex = index

    # Find places for min and max elements in original array
    return (minIndex, maxIndex) # NOT RIGHT

print(find_sorting_window([3,5,9,8,6,11]))
print(find_sorting_window([3,5,9,8,6,11,15,2,13]))
print(find_sorting_window([3,7,15,22,5,29]))


