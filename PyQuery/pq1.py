from pyquery import PyQuery as pq

html = '''
<li>
<a class="cover" href="https://book.douban.com/subject/30475767/"><img src="https://img3.doubanio.com/view/subject/m/public/s32266692.jpg"></a>
<div class="detail-frame">
    <h2>
        <a href="https://book.douban.com/subject/30475767/">人生海海</a>
    </h2>
    <p class="rating">
        <span class="allstar45"></span> 
        <span class="font-small  color-lightgray">
            8.6
        </span>
    </p>
    <p class="color-gray">
        麦家 / 北京十月文艺出版社 / 2019-4-16
    </p>
    <p class="detail">
        一个人在时代中穿行缠斗的一生，离奇的故事里藏着让人叹息的人生况味,既有日常滋生的残酷，也有时间带来的仁慈。麦家新作。
    </p>
</div>
</li>
'''

doc = pq(html)
print(doc('div p.color-gray'))