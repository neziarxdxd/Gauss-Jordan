x = lambda s:([0,]+[int(x or '1-i')for i,x in enumerate(s.split('x'))])[-2:]
print(x("2x+y-5"))