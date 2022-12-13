import time

"""
Given an array of integers, return an array such that each element at i
is the product of every element in the original array excluding the
element at i
"""

"""
def get_product_array(nums):
    products = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        products.append(product)
    return products
"""

"""
def get_product_array(nums):
    product = reduce(lambda x, y: x * y, nums, 1)
    products = [product / i for i in nums]
    return products
"""

def get_product_array(nums):
    n = len(nums)
    left_side = [1] * n
    right_side = [1] * n
    product = 1
    for i in range(n):
        left_side[i] = product
        product *= nums[i]
    product = 1
    for i in range(n-1, -1, -1):
        right_side[i] = product
        product *= nums[i]
    products = []
    for i in range(n):
        products.append(left_side[i] * right_side[i])
    return products

print(get_product_array([3,2,1]))
print(get_product_array(range(1,6)))
"""
start = time.time()
get_product_array([2] * 100000)
end = time.time()
print(end-start, 'seconds')
"""
