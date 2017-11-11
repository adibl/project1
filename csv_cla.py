class Student:
    SCIENCE = [('physics', "5"), ('chemistry', "5"), ('Arabic', "5"), ('biology', "5")]
    MATH = [("math", "5")]
    COPUTER_SCIENCE = [('computer science', "5"), ("computer science", "10")]

    def __init__(self, line):

        self.subject = []
        self.subject.append((line[-2], line[-1]))
        self.properties = []
        self.properties = line[:-2]


    def get_properties(self):
        return self.properties

    def is_same(self, student):
        """
        check if the student line and this student are the same
        :var:student: student line
        :return: true if the student properties are the same and false otherwise
        """
        if student.get_properties() == self.properties:
            return True
        else:
            return False

    def add_subject(self, line):
        """
        add a subject to the student
        :var:line: a list of the subject,level
        :retern: the subjects list
        """
        self.subject.append((line[0], line[1]))
        return self.subject

    def is_amat(self):
        """
        check if the student is amat student
        :return: true if he is amat student and false if not
        """
        is_scientific = False
        is_computer = False
        is_math = False
        for sub in self.subject:
            if sub in Student.SCIENCE:
                is_scientific = True
            if sub in Student.MATH:
                is_math = True
            if sub in Student.COPUTER_SCIENCE:
                is_computer = True
        return is_math and is_scientific and is_computer

    def scientific_subjects(self):
        subjects = []
        for sub in self.subject:
            if (sub in Student.COPUTER_SCIENCE or sub in Student.SCIENCE or sub in Student.MATH):
                subjects.append(sub)
        self.subject = subjects
        return

    def __str__(self):
        line = ""
        for prop in self.properties:
            line += str(prop)+","
        for s in self.subject:
            line += str(s[0])+","+str(s[1]) + ","
        return line[:-1]
