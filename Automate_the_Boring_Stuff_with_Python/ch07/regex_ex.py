import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')#建立Regex物件，找尋相關資料
mo = phoneNumRegex.search('My number is 415-555-4242 or 415-555-1234　')#只找第一個，回傳一個match的物件
mo2 = phoneNumRegex.findall('My number is 415-555-4242 or 415-555-1234　')#找出所有回傳一個string List
# print(type(mo))
# print(mo)
print(mo.group())
print(mo2)
phoneNumRegex2 = re.compile(r'(\d{3})-(\d{3}-\d{4})')#用不同形式建立物件
mo3 = phoneNumRegex2.search('My number is 415-555-4242')
#grpup(0)和grpup() 都是一樣的， group(1)回傳第一個符合的值...group(2)回傳第二個
print(mo3.group(),'\n',mo3.group(1),'\n',mo3.group(2),'\n',mo3.group(0))
#|(pipe可以提供多種可能性的搜尋)
heroRegex = re.compile(r"Batman|Tina Fey")
mo4 = heroRegex.search('Batman and Tina Fey.')
print(mo4.group())
mo5 = heroRegex.search('Tina Fey and Batman.')
print(mo5.group())#一樣是先回傳第一個找到的值
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo6 = batRegex.search('Batmobile lost a wheel')
print(mo6.group())
print(mo6.group(1))
