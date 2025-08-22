# Marks Info
# ------------------------------------------------------------------------------------






class Student:
    def __init__(self,Name):
        print(f'Welcome {Name}')
        self.Marks = []

    def add_Mark (self,Mark):
        self.Marks.append(Mark)

    def avg (self):
        self.avarage = sum(self.Marks)/len(self.Marks)

    def Print_Results(self):
        print(f'Marks = {self.Marks}')
        print(f'Avarage = {self.avarage}')



S1 = Student('Sameh')

S1.add_Mark(90)
S1.add_Mark(95)
S1.add_Mark(89)
S1.avg()
S1.Print_Results()


