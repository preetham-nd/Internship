#single level inheritance
class parent_class:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def method_name(self):
        # implementation
        print(f"Parent class method called with p1={self.p1}, p2={self.p2}")

class child_class(parent_class):
    def __init__(self, p1, p2, p3, p4):
        super().__init__(p1, p2)
        self.p3 = p3
        self.p4 = p4

    def method_name(self):
        # implementation
        print(f"Child class method called with p1={self.p1}, p2={self.p2}, p3={self.p3}, p4={self.p4}")

child_object=child_class(1,2)
child_object.method_name()