# -*- coding: utf-8 -*-\
import sys
sys.path.append('.')
from csv_cla import Student

FILE_DIRECTORY = "csv_westerose.csv"

def text_to_lines(text):
    """
    :var:text: lines of text
    :return: list of tupls, tuple is one raw. the object iside the tupels id splited by ,
    """
    line = ""
    lines = []
    for char in text:
        if char == "\n":
            line = line.split(",")
            lines.append(line)
            line = ""
        else:
            line += char
    lines.append(line)
    return lines


def if_have(new_student, list_of_students):
    for student in list_of_students:
        if new_student[:-2] == student.get_properties():
            return student
    return None


def main():
    """
    Add Documentation here
    """
    with open(FILE_DIRECTORY, 'r') as input_file:
        text = input_file.read()
    lines = text_to_lines(text)
    students = []
    for line in lines:
        if if_have(line, students) is not None:
            if_have(line, students).add_subject(line)
        else:
            students.append(Student(line))












if __name__ == '__main__':
    line2=["rob", "1212", "first", "male", "english", "5"]
    s1 = Student(["rob", "1212", "first", "male", "math", "5"])
    s2 = Student(line2)
    assert s1.is_same(s2)
    assert s1.add_subject(line2) == (['math', 'english'], ['5', '5'])
    assert s1.get_properties() == ["rob", "1212", "first", "male"]
    main()