# cigar_party
def cigar_party(cigars, is_weekend):
  if cigars >= 40 and cigars <= 60:
    return True
  elif cigars >= 40 and is_weekend is True:
    return True
  else:
    return False

# date_fashion
def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  if you >= 8 or date >= 8:
    return 2
  else:
    return 1

# squirrel_play
def squirrel_play(temp, is_summer):
  if is_summer is True and temp >= 60 and temp <= 100:
    return True
  if is_summer is not True and temp >= 60 and temp <= 90:
    return True
  return False

# caught_speeding
def caught_speeding(speed, is_birthday):
  # is_birthday is True; minspeed +5 and maxspeed +5
  # speed <= 60; result 0
  # speed > 60 and speed < 81; result 1
  # speed >= 81; result 2
  minspeed = 0
  maxspeed = 60
  if is_birthday is True:
    minspeed = minspeed + 5
    maxspeed = maxspeed + 5
  if speed <= maxspeed:
    return 0
  minspeed = maxspeed
  maxspeed = maxspeed + 21
  if speed < maxspeed:
    return 1
  if speed > maxspeed:
    return 2

# sorta_sum
def sorta_sum(a, b):
  if a + b >= 10 and a + b <= 19:
    return 20
  else:
    return a + b

# alarm_clock
def alarm_clock(day, vacation):
  if vacation is True:
    if day in range(1,6):
      return '10:00'
    if day is 0 or day is 6:
      return 'off'
  if day in range(1,6):
    return '7:00'
  if day is 0 or day is 6:
    return '10:00'

# love6
def love6(a, b):
  if a == 6 or b == 6 or a+b == 6 or a-b == 6 or b-a == 6:
    return True
  else:
    return False

# in1to10
def in1to10(n, outside_mode):
  if outside_mode is False:
    if n in range(1,11):
      return True
    else:
      return False
  if outside_mode is not False:
    if n in range(2,10):
      return False
    else:
      return True

# near_ten
def near_ten(num):
  mod = num % 10
  if mod+10 <= 12 or mod >= 8:
    return True
  else:
    return False
