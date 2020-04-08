class Person:
    def __init__(self, name,lastname):
        self.Name = name #Name is attributes and name is arguments
        self.Lastname=lastname
        self.Fullname=[name,lastname]
    def sayHi(self):
        print ('Hello', "my name is" , self.Fullname[0])
p = Person("sds","asfas")
p.sayHi()
#在执行p = Person("sds","asas")的时候其实这里床了一个Person类的是实现p 这个类中
#的init方法马上就被调用了。在创建类的时候必须有和方法init匹配的位置参数，这里self指的
#就是创建的实例本身 self是不需要传入的，所以self后面的才是实际需要传入的参数列表我们需要
#传入的2个参数 name lastname这样一旦运行就把Person类实现的属性初始化了。
'''
u_1将已经具有设置好的scores属性。
并且由于__init__规定了实例化时的参数，
若传入的参数数目不正确，
解释器可以报错提醒。你也可以在其内部添加必要的参数检查，
以避免错误或不合理的参数传递。
'''