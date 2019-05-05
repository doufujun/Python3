from pyquery import PyQuery as pq

doc = pq(url='https://www.baidu.com', encoding='utf-8')
print(doc('a'))
print('\n--------\n')
doc('a').remove_class('mnav')
# print(doc('a'))

for i in doc('a').items() :
    print('a标签的内容：', i.text())
    # print('a标签的链接：', i.attr.href)
    print('a标签的class：', i.attr('class'))
    print('-----')