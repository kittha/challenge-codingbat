# first_last6
def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  else:
    return False

# same_first_last
def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[-1]:
    return True
  else:
    return False

# make_pi
def make_pi():
  return [3,1,4]

# common_end
def common_end(a, b):
  if a[0] == b[0] or a[-1] == b[-1]:
    return True
  else:
    return False

# sum3
def sum3(nums):
  total = sum(nums)
  return total

# rotate_left3
def rotate_left3(nums):
    finum = nums[0]
    #print(finum)
    nums = nums[1:]
    nums.append(finum)
    return(nums)

# reverse3
def reverse3(nums):
  return nums[::-1]

# max_end3
def max_end3(nums):
  if nums[0] > nums[-1]:
    bigger = nums[0]
    smaller = nums[-1]
  else:
    bigger = nums[-1]
    smaller = nums[0]
  newlist = list()
  for i in range(len(nums)):
    newlist.append(bigger)
  return newlist

# sum2
def sum2(nums):
  if len(nums) == 0:
    return 0
  if len(nums) < 2:
    return sum(nums)
  if len(nums) >= 2:
    return nums[0] + nums[1]

# middle_way
def middle_way(a, b):
  newlist = list()
  mida = a[1]
  midb = b[1]
  #print(mida)
  #print(midb)
  newlist.append(mida)
  newlist.append(midb)
  return newlist

# make_ends
def make_ends(nums):
  first = nums[0]
  last = nums[-1]
  newlist = list()
  newlist.append(first)
  newlist.append(last)
  return newlist

# has23
def has23(nums):
  for num in nums:
    if num == 2 or num == 3:
      return True
  return False
