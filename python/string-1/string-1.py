# hello_name
def hello_name(name):
  return 'Hello ' + name + '!'

# make_abba
def make_abba(a, b):
  return a + b + b + a

# make_tags
def make_tags(tag, word):
  #print(f'<{tag}>{word}</{tag}>')
  return "<" + tag + ">" + word + "<" + "/" + tag + ">"

# make_out_word
def make_out_word(out, word):
  return out[:2] + word + out[2:]

# extra_end
def extra_end(str):
    str = str[-2::]
    return str * 3

# first_two
def first_two(str):
  if len(str) == 0:
    return ""
  if len(str) < 2:
    return str
  return str[:2]

# first_half
def first_half(str):
  length = len(str)
  return str[:(length/2)]

# without_end
def without_end(str):
  if len(str) >= 2:
    return str[1:len(str)-1]

# combo_string
def combo_string(a, b):
  if len(a) > len(b):
    bigger = a
    smaller = b
  else:
    bigger = b
    smaller = a
  return smaller + bigger + smaller

# non_start
def non_start(a, b):
  if len(a) > 1 and len(b) > 1:
    abria = a[1:]
    abrib = b[1:]
    return abria + abrib
  elif len(a) > len(b):
    bigger = a
    smaller = b
    return bigger[1:]
  elif len(b) > len(a):
    bigger = b
    smaller = b
    return bigger[1:]
  else:
    return ""

# left2
def left2(str):
  if len(str) > 2:
    return str[2:] + str[:2]
  else:
    return str
