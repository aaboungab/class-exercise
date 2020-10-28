class Student:
    def __init__(self, name, age,class_):
        self.name = name
        self.age = age
        self.class_ = "student"

    def test_score(self,test1,test2,test3):
        self.test1 = int(test1)
        self.test2 = int(test2)
        self.test3 = int(test3)
        avg_score = (test1+test2+test3)/3
        return f"Average score across 3 tests is {avg_score:.2f}"

