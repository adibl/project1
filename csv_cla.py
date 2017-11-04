class Student:

    def __init__(self, line):
        self.subject = []
        self.level = []
        self.subject.append(line[-2])
        self.level = line[-1:]
        self.properties = []
        self.properties = line[:-2]


    def get_properties(self):
        return self.properties

    def is_has(self, student):
        if student.get_properties() == self.properties:
            return True
        else:
            return  False

    def add_subject(self, line):
        self.subject.append(line[-2])
        self.level.append(line[-1])

    def Print(self):
        print self.subject






