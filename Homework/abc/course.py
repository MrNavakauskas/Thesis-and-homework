
class Course:
    def __init__(self, name, teacher, duration):
        self.name = name
        self.teacher = teacher
        self.duration = duration

    def teach(self):
        print("Training in progress!")
