#memoization
class Solution(object):
    def robber(self,n,nums,dp):
        if n == 0:
            return nums[n]
        if n<0:
            return 0
        if dp[n]!=-1:
            return dp[n]
        
        pick = nums[n]+self.robber(n-2,nums,dp)#picking so adding nums[n]
        notpick = 0 + self.robber(n-1,nums,dp)#not picking so adding 0
        dp[n] = max(pick,notpick)
        return dp[n]
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp = [-1]*n
        return self.robber(n-1,nums,dp)
  #tabulation
def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        dp=[-1]*n
        dp[0] = nums[0]
        for i in range(1,n):
            if i>1:
                pick = nums[i] + dp[i-2]
            else:
                pick = nums[i]
            notpick = 0 + dp[i-1]
            dp[i] = max(pick,notpick)
        return dp[n-1] 
  #space optimization
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:  # Handling the edge case of an empty array
            return 0
        if n == 1:  # If there's only one house, return its value
            return nums[0]

        # Base cases
        prev1 = max(nums[0], nums[1])  # Max of first two houses
        prev2 = nums[0]  # Only the first house

        # Iterate through the houses starting from the third
        for i in range(2, n):
            # Calculate the maximum amount that can be robbed up to the current house
            current = max(nums[i] + prev2, prev1)
            prev2 = prev1  # Update the values for the next iteration
            prev1 = current

        return prev1  # The answer will be stored in prev1
  
