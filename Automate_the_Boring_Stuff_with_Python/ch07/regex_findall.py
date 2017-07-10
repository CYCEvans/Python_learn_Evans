import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)
print("---------------------")
xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall("12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, "
                  "7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge")
print(mo)
print("---------------------")
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)
print("---------------------")
vowelRegex = re.compile(r'[^aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)