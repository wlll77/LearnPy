# class Person:
#     pass

class Person:
    age = 28    # 累的属性
    __name = "小黑子"

    def print_name(self):
        print(self.__name)

    def test_self(self):    # 方法需要实例化
        print(self.age)
        self.print_name()

    @classmethod      # 类方法 ，类方法不需要实例化
    def class_method_function(cls):
        print(cls.age)


    @staticmethod     # 静态方法  无需参数
    def static_method_function():
        print(Person.age)
        print("现在的名字叫小鸡子")

if __name__ == '__main__':   # 用于隔离下面的代码，不然外部调用的时候，下面的代码也会执行
    # # print(Person.age)
    #
    # person = Person()
    #
    # # print(person.age)
    #
    # # person.print_name()
    #
    # person.test_self()

    # Person.class_method_function()
    # Person.age = 15
    # Person.class_method_function()

    Person.static_method_function()