def max_avg_subarray(nums, k):
  if len(nums)<k:
    return None
  l = 0
  r = l + k #fixed window
  maxSum = sum(nums[l:r])
  runningSum = maxSum
  for i in range(r, len(nums)):
    runningSum += nums[i]
    runningSum -= nums[l]
    l = l+1
    maxSum = max(maxSum, runningSum)
  return maxSum/k
    
