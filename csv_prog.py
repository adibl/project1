# -*- coding: utf-8 -*-\
import sys
sys.path.append('.')
from cla import Student


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
    with open("westerose.csv", 'r') as input_file:
        text = input_file.read()
    lines = text_to_lines(text)
    students = []
    for line in lines:
        if if_have(line, students) is not None:
            if_have(line, students).add_subject(line)
        else:
            students.append(Student(line))













if __name__ == '__main__':
    main()