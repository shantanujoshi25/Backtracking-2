# // Time Complexity : O(2^n)
# // Space Complexity : O(n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        

        def recur(nums,index,arr):

            result.append(arr.copy())
            
           
            
            for i in range(index,len(nums)):
                arr.append(nums[i])
                recur(nums,i+1,arr)
                arr.pop(-1)

        recur(nums,0,[])      
        return result
        