class Test:
    def sayStr(self, str):
        print(str)


if __name__ == '__main__':  # testModule.pyを実行すると以下が実行される（モジュールとして読み込んだ場合は実行されない）
    a = Test()
    a.sayStr("Hello")


def fibo(n):
    result = []
    a = 1
    b = 1

    while b < n:
        result.append(b)
        val = a + b
        b = a
        a = val
    return result

if __name__ == "__main__":
    print("{0}".format(fibo(1000)))


def add(a, b):
    return a * b

def sub(a, b):
    return a / b