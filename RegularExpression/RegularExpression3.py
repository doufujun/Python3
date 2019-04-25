# 匹配目标
import re
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\s.*o$', content)
print(result)
print(result.group())
print(result.group(1))