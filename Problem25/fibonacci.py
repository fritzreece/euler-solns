def fib(n):
    nums = [1,1]
    while n > 2:
        temp = sum(nums)
        nums[0] = nums[1]
        nums[1] = temp
        n -= 1
    return nums[1]
