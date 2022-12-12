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

def get_product_array(nums):
    product = reduce(lambda x, y: x * y, nums, 1)
    products = [product / i for i in nums]
    return products

print(get_product_array(range(1, 6)))
print(get_product_array(range(3, 0, -1)))
#print(get_product_array(range(1, 1000)))

