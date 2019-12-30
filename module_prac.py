"""from testmodule import Test#モジュールをインポート
a = Test()
a.sayStr("Hello world")
import testmodule

print("{0}".format(testmodule.fibo(10000)))

import testmodule

#if __name__ == '__main__':
print(testmodule.add(115, 116))
print(testmodule.sub(1008, 18))"""


import object_prac2
object_prac2.Siro.eat("chicken")
object_prac2.Siro.eatAndSleep("beef")
print("Siro.weight", object_prac2.Siro.weight)

object_prac2.Pochi.eat("chicken")
object_prac2.Pochi.eatAndSleep("pork")
print("Pochi.weight", object_prac2.Pochi.weight)

object_prac2.Choco.eat("pork")
object_prac2.Choco.eatAndSleep("pork")
print("Choco.weight", object_prac2.Choco.weight)

