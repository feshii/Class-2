class student:
    grade = 4
    Name = "kamsi"
    def introduction(self):
        print("I am a student")
    def show(self):
        print("My name is",self.Name)
        print("I am in grade",self.grade)
object = student()
object.introduction()
object.show()
