#练习1 华氏温度转摄氏温度。
def formular(f) :
    # f = 1.8*c + 32
    c = (f - 32) / 1.8
    return c

def printResult(f) :
    print(formular(f))

def main(f) :
    printResult(f)

if __name__ == '__main__' :
    main(100)