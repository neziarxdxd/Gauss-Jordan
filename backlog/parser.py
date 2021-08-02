import re
equation = []
lines = ["1x+1y+0", "1x-1y+0", "1x+0y-3", "0x+1y-0.52=-998"]
for i in lines:
    z = re.findall(r'[\d\.\-\+]+', i)
    number_list = list(map(float,z))
    equation.append(number_list)

print(equation)


# items = [i.strip() for i in re.split('[-+=]', '2x+y=-4')]
# print(items)
# # x = [int(item[0])if item[0].isdigit() else 1 for item in items]
# # print(x)