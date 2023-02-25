class SuperList(list):
    def __len__(self):
        return 1000

my_super_list = SuperList()

print(len(my_super_list))
# my_super_list.append(5)

my_super_list.append(5)
print(my_super_list[0])

print(issubclass(SuperList, list))
print(issubclass(list, object))
