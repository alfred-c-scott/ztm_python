
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))

class BigObject:
    pass

object_0 = BigObject()
object_1 = BigObject()
object_2 = BigObject()

print(type(object_0))
print(type(object_1))
print(type(object_2))
