# count_evens
def count_evens(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            count += 1
    return count

# big_diff
def big_diff(nums):
    small = nums[0]
    big = nums[0]
    for i in range(len(nums)):
        small = min(nums[i],small)
        big = max(nums[i], big)
    #print(big - small)
    return big -small

# centered_average
def centered_average(nums):
    small = nums[0]
    big = nums[0]
    for i in range(len(nums)):
        small = min(nums[i],small)
        big = max(nums[i], big)
    nums.remove(small)
    nums.remove(big)
    nums.sort()
    #print(nums)

    if len(nums) % 2 != 0:
        return nums[len(nums)//2]
    else:
        avg = (nums[(len(nums)//2)-1] + nums[len(nums)//2])/2
        avg = int(avg)
        return avg

# sum13
def sum13(nums):
    sum = 0
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            return 0
        if nums[i] == 13:
            i += 2
            continue
        if nums[i] != 13:
            sum += nums[i]
            i += 1
    #print(sum)
    return sum

'''
def sum13(nums):
    sum = 0
    if nums == 0:
        return 0
    for i in range(len(nums)):
        if nums[i] != 13:
            sum += nums[i]
        if nums[i] == 13 and i < len(nums)-1:
            sum -= nums[i+1]
    if sum < 0:
      sum = 0
    #print(sum)
    return sum
'''

# sum67
def sum67(nums):
    sum = 0
    i = 0
    switch = True # start with switch on mode
    while i < len(nums):
        # con 1: if switch is on; increment sum; continue
        if nums[i] != 6 and switch is not False:
            #print(f'index is {i}/{len(nums)}; test value is {nums[i]}')
            sum += nums[i]
            i += 1
            #print(f'con 1 and sum is {sum}\n')
            continue
        # con 2: switch to off mode; continue
        if nums[i] == 6:
            #print(f'index is {i}/{len(nums)}; test value is {nums[i]}')
            switch = False
            i += 1
            #print(f'con 2 and sum is {sum}\n')
            continue
        # con 3: off mode; continue
        if switch is False and nums[i] != 7:
            #print(f'index is {i}/{len(nums)}; test value is {nums[i]}')
            i += 1
            #print(f'con 3 and sum is {sum}\n')
            continue
        # con 4: switch to on mode; continue
        if switch is False and nums[i] == 7:
            #print(f'index is {i}/{len(nums)}; test value is {nums[i]}')
            switch = True
            i += 1
            #print(f'con 4 and sum is {sum}\n')
            continue
    #print(sum)
    return sum

# has22
def has22(nums):
    if nums is False:
        return False
    old = None
    #print(f'old is {old}\n')
    for i in range(len(nums)):
        if old == nums[i] and old == 2 and nums[i] == 2:
            #print(True)
            return True
        else:
            old = nums[i]
            #print(f'new old is: {old}')
    #print(False)
    return False
