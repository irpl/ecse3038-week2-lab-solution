def parallel(resistors):
  rrs = 0
  for r in resistors:
    rrs += 1/r
  
  p = 1/rrs
  print(p)


parallel([1000, 500, 3000])