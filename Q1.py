def print_numbers(i):
  if ((i%3)==0) and ((i%5)==0):
    return "WorldPeace"
  elif (i%3)==0:
    return "World"
  elif (i%5)==0:
    return "Peace"
  else:
    return i

for n in range(1,101):
  print(print_numbers(n))
