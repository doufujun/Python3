#练习3 输入年份判断是不是闰年
def method(year) :
    if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) :
        print(year, '是闰年')
    else :
        print(year, '不是闰年')

def main() :
    year = int(input('输入一个年份：'))
    method(year)

if __name__ == '__main__' :
    main()