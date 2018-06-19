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

list = ["guru99 get", "guru99 give", "guru Selenium"]
for element in list:
    z = re.match(r"(g\w+)\W(g\w+)", element)
if z:
    print((z.groups()))
    
patterns = ['software testing', 'guru99']
text = 'software testing is fun?'
for pattern in patterns:
    print('Looking for "%s" in "%s" ->' % (pattern, text), end=' ')
    if re.search(pattern, text):
        print('found a match!')
else:
    print('no match')
abc = 'guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)
for email in emails:
    print(email)
