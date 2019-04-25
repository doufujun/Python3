# 泛匹配
import re
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^H.*o$', content)
print(result)