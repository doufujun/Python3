# 非贪婪匹配
import re
content = 'Hello 1234567 World_This is a Regex Demo'
# ?使前面的.*尽可能匹配少的字符
result = re.match('^He.*?(\d+).*o$', content)
print(result)
print(result.group(1))