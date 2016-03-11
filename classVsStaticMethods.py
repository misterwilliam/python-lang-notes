class Parent(object):

    @staticmethod
    def staticMethod():
        print("Parent static method")

    @classmethod
    def classMethod(cls):
        print("Parent class method: %s" % cls)

class ChildOverrider(Parent):

    @staticmethod
    def staticMethod():
        print("ChildOverrider static method")

    @classmethod
    def classMethod(cls):
        print("ChildOverrider class method: %s" % cls)

class ChildNoOverrider(Parent):
    pass

p = Parent()
Parent.staticMethod()
Parent.classMethod()
p.staticMethod()
p.classMethod()

c1 = ChildOverrider()
ChildOverrider.staticMethod()
ChildOverrider.classMethod()
c1.staticMethod()
c1.classMethod()

c2 = ChildNoOverrider()
ChildNoOverrider.staticMethod()
ChildNoOverrider.classMethod()
c2.staticMethod()
c2.classMethod()
