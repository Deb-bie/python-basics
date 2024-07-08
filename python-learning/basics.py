class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_name(self):
        print("My name is " + self.name)

    def my_age(self):
        print("I'm " + str(self.age) + " years old")

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"

me = Person("Debss", 3)
print(me)
me.my_name()
me.my_age()