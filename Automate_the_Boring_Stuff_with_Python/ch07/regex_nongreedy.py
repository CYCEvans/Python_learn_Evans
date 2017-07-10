import re
batRegex = re.compile(r'Bat(wo)?man')#(wo)? 是一種選擇可以出現一次或零次的 wo
mo = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo.group())
print(mo2.group())
print(batRegex.search('The Adventures of Batwowowowoman'))#出現多次沒有找到
print("====================================")
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo3=phoneNumRegex.search("This is my number: 412-567-8892 , call me ~")
print(mo3.group())
print(phoneNumRegex.search("This is my number: 555-7848 , call me ~"))#找不到
phoneNumRegex2 = re.compile(r'(\d{3}-)?\d{3}-\d{4}')#find it!
mo4 = phoneNumRegex2.search("This is my number: 555-7848 , call me ~")
print(mo4.group())
print("====================================")
batRegex2=re.compile(r'Bat(wo)*man')#(wo)? 是一種選擇可以出現多次或零次的 wo
mo1 = batRegex2.search('The Adventures of Batman')
mo2 = batRegex2.search('The Adventures of Batwoman')
mo3 =batRegex2.search('The Adventures of Batwowowowoman')
print(mo1.group(),mo2.group(),mo3.group())
print("====================================")
haRegex = re.compile(r'(Ha){3,5}')#找3-5個Ha
mo1=haRegex.search('HaHaHa')
mo2=haRegex.search('HaHaHaHa')
mo3=haRegex.search('HaHaHaHaHaHaHaHaHa')#最多5個
print(mo1.group(),mo2.group(),mo3.group())

digitRegex = re.compile(r'(\d){3,5}')
mo1=digitRegex.search('123456789')#搜尋到最大值
print(mo1.group())
digitRegex = re.compile(r'(\d){3,5}?')
mo2=digitRegex.search('123456789')#搜尋到最小值，因為non-greedy。
print(mo2.group())
