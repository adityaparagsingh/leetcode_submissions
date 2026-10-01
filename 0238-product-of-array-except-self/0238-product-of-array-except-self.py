class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        left_arr = [0]*n
        left_product = 1

        right_arr = [0]*n
        right_product = 1

        answer = []

        for i in range (n):
            j = -i - 1
            left_arr[i] = left_product
            right_arr[j] = right_product
            left_product *= nums[i]
            right_product *= nums[j]
        
        for i in range (n):
            answer.append(left_arr[i]*right_arr[i])
        return answer