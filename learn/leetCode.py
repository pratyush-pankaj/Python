class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        for i in range(0,len(nums)):
            rem = target - nums[i]
            search = binary_search(nums,0,len(nums)-1,rem)
            if search != -1:
                return [i,search]


    def binary_search(self, arr, low, high, x):
 
        # Check base case
        if high >= low:
    
            mid = (high + low) // 2
    
            # If element is present at the middle itself
            if arr[mid] == x:
                return mid
    
            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                return binary_search(arr, low, mid - 1, x)
    
            # Else the element can only be present in right subarray
            else:
                return binary_search(arr, mid + 1, high, x)
    
        else:
            # Element is not present in the array
            return -1
            
        