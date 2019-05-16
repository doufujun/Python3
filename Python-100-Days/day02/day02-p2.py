#练习2 输入圆的半径计算计算周长和面积。
import math

def perimeter(radius) :
    #圆周长=半径x2Π
    p = radius * math.pi * 2
    return p

def area(radius) :
    #圆面积 = 2 * pi * r * r
    a = 2 * math.pi * radius * radius
    return a

def main() :
    r = float(input('Enter a radius: '))
    print('周长：', perimeter(r))
    print('面积：', area(r))

if __name__ == '__main__' :
    main()