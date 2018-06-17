import re

#The first expression is ^ and w+ 
#^: matches the starting of a string
#w+: matches the alphanumaric characters in a string
xx = "guru99, education is fun"
r1 = re.findall(r"^\w+",xx)
print(r1)

#s:used to create a space in the string 
r2 = re.split(r"\s",xx)
r3 = re.split(r"s",xx)
print(r2)
print(r3)
