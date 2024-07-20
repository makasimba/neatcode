from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_index_product = []
        pre_product = 1
        for n in nums:
            pre_product = pre_product * n
            pre_index_product.append(pre_product)

        post_index_product = []
        post_product = 1
        for n in nums[::-1]:
            post_product = post_product * n
            post_index_product.append(post_product)
        
        post_index_product = post_index_product[::-1]
        product_except_self = []
        for i, n in enumerate(nums):
            pre_index = i - 1
            post_index = i + 1

            if pre_index < 0:
                pre_product = 1
            else:
                pre_product = pre_index_product[pre_index]
            
            if post_index > len(nums)-1:
                post_product = 1
            else:
                post_product = post_index_product[post_index]
            
            p = pre_product * post_product 
            product_except_self.append(p)
        return product_except_self

# Time complexity: O(n)
# Space complexity: O(n)

tests = [[1,2,4,6], [-1,0,1,2,3]]
solutions = [[48,24,12,8], [0,-6,0,0,0]]

for t, s in zip(tests, solutions):
    solution = Solution()
    a = solution.productExceptSelf(t)
    print(a, s)
    