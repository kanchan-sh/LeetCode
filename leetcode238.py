# Given an integer array nums, return an array answer such that answer[i] is equal to 
# the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# def product_except_self(nums):
#     l = len(nums)
#     product_list = []
#     for i in range(l):
#         product = 1
#         for  j in range(l):
#             if nums[i] != nums[j]:
#                 product*=nums[j]
#         product_list.append(product)
#     return product_list
def product_except_self(nums):
    left = []
    right = []
    p = 1
    for i in nums:
        p*=i
        left.append(p)
    p = 1
    for i in nums[::-1]:
        p*=i
        right.append(p)
    print(left)
    print(right)



 
    
nums = [1,2,3,4]
# nums = [0,0]
print(product_except_self(nums))