class Data:
    '''初期化メソッド（インスタンス変数とデータ）'''
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]
    '''インスタンスメソッド'''
    def change_data(self, index, n):
        self.nums[index] = n


'''インスタンス変数 num をクラスの外側から直接変更する(client)。'''
data1 = Data()
data1.nums[0] = 100
print(data1.nums)

'''インスタンス変数 num をクラスで定義したメソッドを使って変更する。'''
data2 = Data()
data2.change_data(0, 100)
print(data2.nums)


class PublicPrivateExample:
    '''初期化メソッド（インスタンス変数の定義）'''
    public = "safe"
    __unsafe = "unsafe" #変数が _ で始まっています。
    '''client が使うべきじゃないメソッド'''
    def __unsafe_method(self): #メソッドが _ で始まっています。
        return "It's " + self.__unsafe
    '''client が使っていいメソッド'''
    def public_method(self):
        print(self.__unsafe_method())


data3 = PublicPrivateExample()
print(data3.public)
data3.public_method()
data3.public = 100
data3.__unsafe = 100
print(data3.public)
data3.public_method()

print("Hello World") #文字列(str)型
print(100) #整数(int)型
print(100.1) #浮動小数点(float)型

class Sample:
    __name = "Yamada"

    def __hello(self):
        return "Hello! I'm " + self.__name

    def printhello(self):
        print(self.__hello())

a = Sample()

#print(a.__name)      # クラス変数nameを直接参照して表示
#print(a.__hello())   # hello()メソッドの戻り値を表示
a.printhello()     # printhello()メソッドを呼び出す