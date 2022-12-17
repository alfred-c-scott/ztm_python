class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat_0 = Cat('furry', 5)
cat_1 = Cat('fluffy', 2)
cat_2 = Cat('Young\'en', 1)

list_of_cats = [cat_0, cat_1, cat_2]

def oldest_cat(cats):
    age_of_oldest = 0
    for cat in cats:
        if cat.age > age_of_oldest:
            age_of_oldest = cat.age
    return age_of_oldest

print(oldest_cat(list_of_cats))


# I wanted to see if I could figure out a way to
# return the cat as an object and came up with this

def return_cat(cats):
    cat = cats[0]
    for c in cats:
        if c.age > cat.age:
            cat = c
    return cat

oldest = return_cat(list_of_cats)
print(f'the oldest cat is {oldest.name}, and is {oldest.age} years old')