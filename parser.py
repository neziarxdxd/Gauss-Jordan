import re
equation = []
lines = ["1x+1y+0 =5", "1x-1y+0", "1x+0y-3", "0x+1y-0.5","2x+3y=5"]
for i in lines:
    z = re.findall(r'[\d\.\-\+]+', i)
    equation.append(z)

c = list(map(int,equation[0]))
print(c)