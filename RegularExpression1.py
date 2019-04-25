# 最常规匹配
import re
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}.*o', content)
print(result)
print('con length:', len(content))
#group打印匹配的内容
print('group:', result.group())
#span打印已匹配的长度
print('span:', result.span())