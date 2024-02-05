def parallel(resistors):
  rrs = 0
  for r in resistors:
    rrs += 1/r
  
  p = 1/rrs
  print(p)


def potential_divider(v, resistors):
  for r in resistors:
    vr = (v * r)/sum(resistors)
    print(str(vr) + "v")
