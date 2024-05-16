# make_bricks
def make_bricks(small, big, goal):
  if (small*1) + (big*5) < goal:
      return False
  # smalllong = small * 1
  # biglong = big * 5
  needbig = goal // 5
  remain = goal - (needbig * 5)
  #print(f'remain is: {remain}')
  tot = remain - small
  #print(f'tot is: {tot}')
  if tot <= 0:
    #print('True')
    return True
  else:
    #print('False')
    return False

# lone_sum
def lone_sum(a, b, c):
  if a == b and b == c:
    a = 0
    b = 0
    c = 0
  if a == b:
    a = 0
    b = 0
  if b == c:
    b = 0
    c = 0
  if a == c:
    a = 0
    c = 0
  tot = a + b + c
  #print(tot)
  return tot

#lone_sum(1, 2, 3) # 6
#lone_sum(3, 2, 3) # 2
#lone_sum(3, 3, 3) # 0

# lucky_sum
def lucky_sum(a, b, c):
  luckylist = list()
  luckylist.append(a)
  luckylist.append(b)
  luckylist.append(c)
  #print(luckylist)
  numsum = 0
  for num in luckylist:
    if num != 13:
      numsum += num
    if num == 13:
      break
  #print(numsum)
  return numsum

#lucky_sum(1, 2, 3) # 6
#lucky_sum(1, 2, 13) # 3
#lucky_sum(1, 13, 3) # 1

# no_teen_sum
def no_teen_sum(a, b, c):
    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)
    tot = a+b+c
    return tot

def fix_teen(n):
    if n >= 13 and n <= 14 or n >= 17 and n <= 19:
        return 0
    else:
        return n

# round_sum
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    # function that check num to round up or round down
    # we can check by using modulo %
    # in case of num % 10 >= 5; then round up
    if num % 10 >= 5:
        num = num + (10 - (num % 10))
        return num
    # in case of num % 10 < 5; then round down
    else:
        num = num - (num % 10)
        return num

#round_sum(16, 17, 18) # 60
#round_sum(12, 13, 14) # 30
#round_sum(6, 4, 4) # 10
#round10(18)

# close_far
def close_far(a, b, c):
    #print(f'unit test sample is a={a} b={b} c={c}')
    # if close is True and far is True; then return True
    if chk_con1(a, b, c) is True and chk_con2(a, b, c) is True:
        #print('close_far is True')
        return True
    else:
        #print('close_far is False')
        return False


# as b; con1: diff 1 to a; con2: diff 2 to a and c
# as c; con1: diff 1 to a; con2: diff 2 to a and b
def chk_con1(a, b, c):
    # check con1 close
    if abs(c - a) <= 1 or abs(b - a) <= 1:
        #print('con1 True')
        return True
    else:
        #print('con1 False')
        return False

def chk_con2(a, b, c):
    # check con2 far
    #print(f'c-b is {abs(c-b)}')
    #print(f'c-a is {abs(c-a)}')
    #print(f'b-a is {abs(b-a)}')
    #print(f'c-b >= 2 is {abs(c-b) >= 2}')
    #print(f'c-a >= 2 is {abs(c-a) >= 2}')
    #print(f'b-a >= 2 is {abs(b-a) >= 2}')
    if abs(c - a) >= 2 and abs(c - b) >= 2:
        #print('con2.1 True')
        return True
    elif abs(b - a) >= 2 and abs(c - b) >= 2:
        #print('con2.2 True')
        return True
    else:
        #print('con2 False')
        return False

#close_far(1, 2, 10) # True
#close_far(1, 2, 3) # False
#close_far(4, 1, 3) # True
#close_far(10, 8, 9) # False

# make_chocolate
def make_chocolate(small, big, goal):
    #print(f'unit test for {small} {big} {goal}')
    # Guardian check if resource available
    if (small * 1) + (big * 5) < goal:
        #print(f'{small} {big} {goal} result: -1')
        return -1
    # check if: goal can deduct with 5kg bar or not?
    if goal // 5 >= 1:
        rem = goal
        for i in range(big):
            if goal - 5 >= 0 and rem >= 5:
                rem = rem - 5
        #print(f'rem con 1 is {rem}')
    else:
        # if goal cant deduct with 5 kg bar; set remaining var <= goal
        rem = goal
        #print(f'rem con 2 is {rem}')
    # how should we know the number of small bars to use?
    # if rem - small > 0; mean it can't be done; return -1;
    if rem - small > 0:
        #print(f'sbtouse is: -1')
        return -1
    # if rem - small == 0; sbtouse = small; return sbtouse;
    if rem - small == 0:
        #print(f'sbtouse (small) is: {small}')
        return small
    # if rem - small < 0; sbtouse = rem; return rem
    if rem - small < 0:
        #print(f'sbtouse (rem) is: {rem}')
        return rem
