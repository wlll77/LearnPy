class Animal:
    def __init__(self):
        pass

    def eat(self):
        print("作为一只动物，我每天都要吃东西")

    def speak(self):
        print("喵喵喵")

class  Dog(Animal):                     #继承Animal,可以用父类的方法
    def love(self):                     #也可以定义自己的方法
        print("我想谈恋爱")
    def speak(self):
        print("我想中1000w")             #多态，即重写，可以改写父类的方法


class Cat(Animal):
    pass

dog = Dog()
dog.eat()
dog.love()
dog.speak()

cat = Cat()
cat.speak()