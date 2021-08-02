import re
items = [i.strip() for i in re.split('[-+=]', '+2x-5y=-4')]
print(items)
# x = [int(item[0])if item[0].isdigit() else 1 for item in items]
# print(x)