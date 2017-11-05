class Student:
    SCIENCE_SUBJECTS = [('physics', "5"), ('chemistry', "5"), ('Arabic', "5"), ('biology', "5")]
    SCIENCE_SUBJECTS_MUST_HAVE = [("math", "5")]
    SCIENCE_SUBJECTS_NEED_ONE = [('computer science', "5"), ("computer science", "10")]

    def __init__(self, line):

        self.subject = []
        self.subject.append((line[-2], line[-1]))
        self.properties = []
        self.properties = line[:-2]

    def get_properties(self):
        return self.properties

    def is_same(self, student):
        if student.get_properties() == self.properties:
            return True
        else:
            return False

    def add_subject(self, line):
        self.subject.append((line[0], line[1]))
        return self.subject

    def is_amat(self):
        is_sientific = False
        is_computer = False
        is_math = False
        for sub in self.subject:
            if sub in Student.SCIENCE_SUBJECTS:
                is_sientific = True
            if sub in Student.SCIENCE_SUBJECTS_MUST_HAVE:
                is_math =True
            if sub in Student.SCIENCE_SUBJECTS_NEED_ONE:
                is_computer = True
        if is_math and is_sientific and is_computer:
            return True
        return False



    def __str__(self):
        line = str(self.properties)
        line += str(self.subject)
        line += str(self.level)
        return line
