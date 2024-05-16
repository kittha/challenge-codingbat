# string_times
def string_times(str, n):
  return str * n

# front_times
def front_times(str, n):
  frstr = str[:3]
  return frstr * n

# string_bits
def string_bits(str):
  new_word = ''
  for i in range(len(str)):
    if i % 2 == 0:
      new_word = new_word + str[i]
  return new_word

# string_splosion
def string_splosion(str):
  tsum = ''
  for i in range(len(str)+1):
    for t in str[:i]:
      tsum += t
  return tsum

# last2
def last2(str):
  count = 0
  newstr = str[:len(str)-2]
  last2 = str[len(str)-2:]
  for i in range(len(newstr)):
    sub = str[i:i+2]
    if sub == last2:
      count += 1
  return count

# array_count9
def array_count9(nums):
  count = 0
  for num in nums:
    if num == 9:
      count += 1
  return count

# array_front9
def array_front9(nums):
  if len(nums) == 0:
    return False

  end = len(nums)
  if end > 4:
    end = 4

  for i in range(end):
    if nums[i] == 9:
      return True
    continue
  return False

# array123
def array123(nums):
  for i in range(len(nums)):
    if i+2 < len(nums) and nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False

# string_match
def string_match(a, b):
  if len(a) > len(b):
    bigger = a
    smaller = b
  else:
    bigger = b
    smaller = a
  count = 0
  for i in range(len(bigger)-1):
    if smaller[i:i+2] == bigger[i:i+2]:
      count += 1
    continue
  return count
