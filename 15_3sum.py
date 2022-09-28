class Solution(object):
    def threeSum(self, nums):
      nums.sort() 
      res = []
      n = len(nums)
      
      for ind, val in enumerate(nums):
          if ind > 0 and val == nums[ind-1]:
              continue
          
          low, high  = ind+1, n-1
          
          while low < high:
              t_sum = val + nums[low] + nums[high]
              if t_sum > 0:
                  high -= 1
              elif t_sum < 0:
                  low += 1
              else:
                  res.append([val, nums[low], nums[high]])
                  low += 1
                  while nums[low] == nums[low-1] and low < high:
                      low += 1
      return res