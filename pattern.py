import re
string = '''
11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   
'''
pattern = re.compile(r":?.(#[0-9a-fA-f]{6}|#[0-9a-fA-f]{3})")
matches = pattern.findall(string)
for match in matches:
    print(*match)