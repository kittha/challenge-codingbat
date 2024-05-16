# sleep_in
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

# monkey_trouble
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile or not a_smile and not b_smile:
    return True
  else:
    return False

# sum_double
def sum_double(a, b):
  if a == b:
    return (a+b)*2
  else:
    return a+b

# diff21
def diff21(n):
  if n > 21:
    return abs((21-n)*2)
  else:
    return abs(21-n)

# parrot_trouble
def parrot_trouble(talking, hour):
  if talking and (hour < 7 or hour > 20):
    return True
  else:
    return False
# trouble is True
# if parrot is talking and hour is 0-7 or 20-23

# makes10
def makes10(a, b):
  if (a + b) == 10 or a == 10 or b ==10:
    return True
  else:
    return False

# near_hundred
def near_hundred(n):
  return abs(100-n) <= 10 or abs(200-n) <= 10

# pos_neg
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

# not_string
def not_string(str):
  if len(str) >= 3 and str[:3] == 'not':
    return str
  else:
    return 'not '+str

# missing_chart
def missing_char(str, n):
  front = str[:n]
  back = str[n+1:]
  return front+back

# front_back
def front_back(str):
  if len(str) <= 1:
    return str

  last = str[-1]
  middle = str[1:len(str)-1]
  first = str[0]
  return last+middle+first

# front3
def front3(str):
  str3cha = str[0:3]
  return str3cha*3
