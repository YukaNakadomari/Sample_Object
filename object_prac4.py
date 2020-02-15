class animal(object):
    def __init__(self, name, food, action):
       self.name = name
       self.food = food
       self.action = action

class sousyoku(animal):
    def __init__(self, name, food, action):
        super(sousyoku, self).__init__(name, food, action)
        self.action = action

class nikusyoku(animal):
    def __init__(self, name, food, action, hunt):
        super(nikusyoku,self).__init__(name, food, action)
        self.hunt = hunt


    def hunting(self):
        if self.action == '狩り':
            print(self.name,'狩りをする' )
            emono.action = '逃げる'
            print(emono.name, emono.action)
            print(self.name, self.action, self.hunt)
            if self.hunt == '成功':
                self.action = '食べる'
                print(self.name, self.food, self.action)
                emono.action = '食べられた'
                print(emono.name, emono.action)
                print()
            else:
                self.hunt = '失敗'
                self.action = '寝る'
                emono.action = '逃げきれた'
                print(emono.name, emono.action)
                print(self.name, self.action)
                print()
        else:
            self.action = '寝る'
            print(self.name, self.action)
            print( )




sample1 = sousyoku('シマウマ', '草', '食べる')
sample2 = sousyoku('鹿', '木の皮', '食べる')
sample3 = nikusyoku('虎', '肉', '寝る', '')
sample4 = nikusyoku('狼', '肉', '寝る', '')
emono = sample1
"""print(sample1.name, sample1.food, sample1.action)
print(sample2.name, sample2.food, sample2.action)
print(sample3.name,  sample3.action)
print(sample4.name,  sample4.action)


sample3.action = '狩り'
sample3.hunt = '成功'
sample3.hunting()
sample4.action = '狩り'
sample4.hunt = '失敗'
sample4.hunting()

emono = sample2
sample3.action = '狩り'
sample3.hunt = '失敗'
sample3.hunting()

sample4.action = '狩り'
sample4.hunt = '成功'
sample4.hunting()

sample3.action = 'hh'
sample3.hunt = '成功'
sample3.hunting()"""