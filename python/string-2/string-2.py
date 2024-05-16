# double_chart
def double_char(str):
  line = ''
  for a in str:
    line = line+a*2
  return line

# count_hi
def count_hi(str):
  newstr = str.replace(" ","")
  count = 0
  for i in range(len(str)):
    if str[i:i+2] == 'hi':
      count += 1
  #print(count)
  return count

# cat_dog
def cat_dog(str):
  if catcount(str) == dogcount(str):
    return True
  else:
    return False

def catcount(str):
  catcount = 0
  for i in range(len(str)):
    #print(f'i={str[i]} i:i+3={str[i:i+3]}')
    if str[i:i+3]  == 'cat':
      catcount += 1
  return catcount

def dogcount(str):
  dogcount = 0
  for i in range(len(str)):
    #print(f'i={str[i]} i:i+3={str[i:i+3]}')
    if str[i:i+3]  == 'dog':
      dogcount += 1
  return dogcount

# count_code
def count_code(str):
  count = 0
  for i in range(len(str)-3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      count += 1
  return count

# end_other
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if len(a) > len(b):
    bigger = a
    smaller = b
  else:
    bigger = b
    smaller = a
  #print(bigger, smaller)
  for i in range(len(bigger)):
      #print(f'smaller is {smaller}')
      #print(f'bigger is {bigger}')
      if smaller == bigger[i:i+3]:
          #print('True')
          return True
  return False

# xyz_there
def xyz_there(str):
    remchar = str.replace('.xyz','')
    #print(remchar)
    status = False
    for i in range(len(remchar)):
        if remchar[i:i+3] == 'xyz':
            status = True
    #print(status)
    return status

#text = 'abcxyz'
#text = 'abc.xyz'
#text = 'xyz.abc'
#text = '1.xyz.xyz2.xyz'
#text = '12xyz'

#xyz_there(text)
