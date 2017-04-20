# FileName:BaseModel.py
class BaseClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print "baseclass is inited"

    def speak(self, name):
        print "base class is speak:%s" %name

if (__name__=='__main__'):
    b = BaseClass()