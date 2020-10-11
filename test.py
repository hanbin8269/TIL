class Test():
    def __init__(self):
        self.aaa = 1
        self._bbb = 2
        self.__ccc = 3
    
    def hello(self):
        print('hello')

t = Test()

setattr(t,'aaa',123)
print(t.aaa)

def callback():
    print('goodbye :)')

setattr(t,'hello',callback)
t.hello()