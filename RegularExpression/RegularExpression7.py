# 转义
import re
content = 'price is $5.00'
# 使用\来转义特殊字符
result = re.match('price is \$5\.00', content)
print(result)
print(result.group())