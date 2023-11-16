class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            n = len(nums)
            total_product = 1
            zero_count = 0

            # Calculate the total product and count the number of zeros
            for num in nums:
                if num == 0:
                    zero_count += 1
                else:
                    total_product *= num

            products = []

            # If there are more than one zero, all products will be zero except at the zero indices
            if zero_count >= 2:
                products = [0] * n
            # If there is only one zero, the product is zero at the zero index and total product at others
            elif zero_count == 1:
                products = [0 if num != 0 else total_product for num in nums]
            # If there are no zeros, divide the total product by each number to get the result
            else:
                for num in nums:
                    products.append(total_product // num)

            return products