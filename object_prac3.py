import object_prac4

print(object_prac4.sample1.name, object_prac4.sample1.food, object_prac4.sample1.action)
print(object_prac4.sample2.name, object_prac4.sample2.food, object_prac4.sample2.action)
print(object_prac4.sample3.name,  object_prac4.sample3.action)
print(object_prac4.sample4.name,  object_prac4.sample4.action)

object_prac4.emono = object_prac4.sample1
object_prac4.sample3.action = '狩り'
object_prac4.sample3.hunt = '成功'
object_prac4.sample3.hunting()

object_prac4.emono = object_prac4.sample2
object_prac4.sample3.action = '狩り'
object_prac4.sample3.hunt = '失敗'
object_prac4.sample3.hunting()


object_prac4.emono = object_prac4.sample1
object_prac4.sample4.action = '狩り'
object_prac4.sample4.hunt = '失敗'
object_prac4.sample4.hunting()

object_prac4.emono = object_prac4.sample2
object_prac4.sample4.action = '狩り'
object_prac4.sample4.hunt = '成功'
object_prac4.sample4.hunting()

