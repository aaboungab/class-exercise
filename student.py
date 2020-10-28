class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    class_ = "student"

    def test_score(self,score_1,score_2,score_3):
        total = score_1 + score_2 + score_3
        avg_score = total/3
        return f"Average score across 3 tests is {avg_score:.2f}"

Anas = Student("Anas", 24)
print(Anas.class_)
print(Anas.test_score(80,85,95))