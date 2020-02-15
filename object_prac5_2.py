from object_prac5 import My_Data

a = My_Data("名前", "性別", "a", "2", "1")
a.My_Data_Display()

import object_prac4
import random
print(object_prac4.sample1.name, object_prac4.sample1.food, object_prac4.sample1.action)
print(object_prac4.sample2.name, object_prac4.sample2.food, object_prac4.sample2.action)
print(object_prac4.sample3.name,  object_prac4.sample3.action)
print(object_prac4.sample4.name,  object_prac4.sample4.action)

object_prac4.emono = object_prac4.sample1
object_prac4.sample3.action = random.choice(('狩り', '寝る'))
object_prac4.sample3.hunt = random.choice(('成功', '失敗'))
object_prac4.sample3.hunting()

object_prac4.emono = object_prac4.sample2
object_prac4.sample3.action = random.choice(('狩り', '寝る'))
object_prac4.sample3.hunt = random.choice(('成功', '失敗'))
object_prac4.sample3.hunting()


object_prac4.emono = object_prac4.sample1
object_prac4.sample4.action = random.choice(('狩り', '寝る'))
object_prac4.sample4.hunt = random.choice(('成功', '失敗'))
object_prac4.sample4.hunting()

object_prac4.emono = object_prac4.sample2
object_prac4.sample4.action = random.choice(('狩り', '寝る'))
object_prac4.sample4.hunt = random.choice(('成功', '失敗'))
object_prac4.sample4.hunting()

