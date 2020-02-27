'''親クラス'''
class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    def print_size(self):
        print(f"横は{self.width}cm, 縦は{self.len}cmです。")

'''子クラス'''
class Square(Shape):
    pass

'''確認してみましょう。'''
square = Square(10, 10)
square.print_size()


'''親クラス'''
class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print(f"横は{self.width}cm, 縦は{self.len}cmです。")

'''子クラス'''
class Square(Shape):
    def area(self):
        return f"面積 {self.width * self.len}㎠"

'''確認してみましょう。'''
square = Square(10, 16)
square.print_size()
print(square.area())


'''親クラス'''
class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print(f"横は{self.width}cm, 縦は{self.len}cmです。")

square = Shape(13, 13)
square.print_size()

print(square.width * square.len, "㎠")
'''子クラス'''
class Square(Shape):
    def print_size(self):
        area = self.width * self.len
        return f"横は{self.width}cm, 縦は{self.len}cm、面積は{area}㎠です。"

'''確認してみましょう。'''
square = Square(17, 13)
print(square.print_size())
