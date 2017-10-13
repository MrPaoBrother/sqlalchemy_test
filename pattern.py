#-*-coding:utf8-*-

import re

pattern1 = r'^\d{3}\-\d{3,8}$'

str = '010-55668'

if re.match(pattern1 , str):
    print "ok"
else:
    print "匹配失败。。。。"


str1 = 'a,b,c,v  ;;;;;;;;;;;;; s                s,r'
pattern2 = r'[\s\,\;]+'
result1 = re.split(pattern2 , str1)
print result1


str2 = '1256000'
pattern3 = r'^(\d+?)(0*)$'
result2 = re.match(pattern3 , str2).groups()
print result2

#下面是先预编译

str3 = '456789-111aaa'
pattern4 = r'(\d+)\-([\d\w]+)'
yubianyi = re.compile(pattern4)
#result3 = yubianyi.match(str3).groups()
if yubianyi.match(str3):
    print "okok"
else:
    print "failed"