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
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe" #変数が _ で始まっています。
    '''client が使っていいメソッド'''
    def public_method(self):
        pass
    '''client が使うべきじゃないメソッド'''
    def _unsafe_method(self): #メソッドが _ で始まっています。
        pass

data3 = PublicPrivateExample()
print(data3.public)
print(data3._unsafe)
data3.public = 100
print(data3.public)
print(data3._unsafe)

print("Hello World") #文字列(str)型
print(100) #整数(int)型
print(100.1) #浮動小数点(float)型 