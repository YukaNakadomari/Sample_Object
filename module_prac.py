from testmodule import Test#モジュールをインポート
a = Test()
a.sayStr("Hello world")
import testmodule

print("{0}".format(testmodule.fibo(10000)))

import testmodule

#if __name__ == '__main__':
print(testmodule.add(115, 116))
print(testmodule.sub(1008, 18))