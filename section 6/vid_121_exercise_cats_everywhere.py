class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat_1 = Cat('Austin', 5)
cat_2 = Cat('Fargo', 3)
cat_3 = Cat('Windle', 2)

list_of_cats = [cat_1, cat_2, cat_3]


def oldest(cats):
    tmp_cat = Cat('tmp', 0)
    for cat in cats:
        if cat.age > tmp_cat.age:
            tmp_cat = cat

    return tmp_cat


oldest_cat = oldest(list_of_cats)

print(f'the oldest cat is {oldest_cat.name}, he/she is {oldest_cat.age}')