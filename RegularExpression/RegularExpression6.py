# 匹配模式
import re
content = '''Hello 1234567 World_This
is a Regex Demo
'''
# re.S可以使得正则可以匹配到换行符
result = re.match('.*', content, re.S)
print(result)
print(result.group())