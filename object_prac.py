class Apple:
    def __init__(self, w, c):
        self.weight = w
        self.color = c

apple1 = Apple(10, "dark red")

print(apple1.weight)
print(apple1.color)

apple1.weight = 20  #値を変更しています。
apple1.color = "light red" #値を変更しています。
print(apple1.weight)
print(apple1.color)

class Apple:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print(w, c)
apple2 = Apple(6, "light red")
apple3 = Apple(9, "dark red")
apple4 = Apple(12, "yellow")


class Rectangle:
    # Rectangle クラスの共通属性（インスタンス変数）
    def __init__(self, w, h):
        self.width = w
        self.height = h

# Rectangle クラスの面積計算メソッド area()
    def area(self):
        return self.width * self.height


# Rectangle クラスのサイズの変換メソッド change_size()
    def change_size(self, w, h):
        self.width = w
        self.height = h


rect1 = Rectangle(15, 20)  # インスタンスを作ります。
print(rect1.area())  # メソッドを使って面積を計算します。

rect1.change_size(15, 25)  # メソッドを使ってサイズを変更します。
print(rect1.area())  # メソッドを使って面積を計算します。