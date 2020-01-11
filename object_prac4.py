class Calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def exz(self):
        return self.x * self.y


class NewCalc(Calc):  # Calc クラスを継承してサブクラスを定義
    def add(self):  # add メソッドをオーバーライド
        print(self.x + self.y)

    def sub(self):
        print(self.x - self.y)

    def exz(self):
        print(self.x / self.y)


if __name__ == "__main__":
    nc = NewCalc(1, 2)  # NewCalc クラスのインスタンスを生成
    nc.add()  # 3
    nc.sub()  # -1
    nc.exz()