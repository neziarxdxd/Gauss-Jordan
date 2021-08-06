import re

array = "6a  -  5b  =  10"
equation = array.split()
array = "".join(equation)
z = re.findall(r'[\d\.\-\+]+', array)
print(z)
