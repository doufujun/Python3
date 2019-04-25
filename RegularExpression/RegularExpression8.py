# re.search
import re
content = 'abcd I dont know acac'
# 使用\来转义特殊字符
r1 = re.match('I.*ow', content)
print(r1)
# print(result.group())
r2 = re.search('I.*ow', content)
print(r2)