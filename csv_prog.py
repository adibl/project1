# -*- coding: utf-8 -*-\
"""
writer: adi bleyer
date: 11/11/2017
this file contain the main prog.
the file have funcsions that take care of csv files
and funcsions thet hundle the student class.
the main take a csv file of students
and return new one that contain only amat students
"""
from csv_cla import Student
import sys
sys.path.append('.')


FILE_DIRECTORY = "csv_westerose.csv"
NEW_FILE_NAME = "amat.csv"


def text_to_lines(text):
    """
    :var:text: lines of text
    :return: list of tupls, tuple is one raw.
    the object iside the tupels id splited by ,
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
    """
    cack if the student is exzisting on the lise
    :var:new_stident: line of a student
    :var:list_of_students: list of students
    :return: None if the student is not in the list.
    if it is return the student
    """
    for student in list_of_students:
        if new_student[:-2] == student.get_properties():
            return student
    return None


def main():
    """
    open the csv file.
    read all the students from him.
    create a new file of amat students only
    the new file contain just the amat subjects
    """
    with open(FILE_DIRECTORY, 'r') as input_file:
        text = input_file.read()
    lines = text_to_lines(text)
    students = []
    for line in lines:
        if if_have(line, students) is not None:
            if_have(line, students).add_subject(line[-2:])
        else:
            students.append(Student(line))
        amat = []
    for student in students:
        if student.is_amat():
            amat.append(student)
    for student in amat:
        student.scientific_subjects()
    new_file = open(NEW_FILE_NAME, "w")
    for s in amat:
        new_file.write(str(s)+"\n")
    new_file.close()


if __name__ == '__main__':
    line2 = ["rob", "1212", "first", "male", "english", "5"]
    s1 = Student(["rob", "1212", "first", "male", "math", "5"])
    s2 = Student(line2)
    assert s1.is_same(s2)
    assert s1.add_subject(line2[-2:]) == ([("math", "5"), ("english", "5")])
    assert s1.get_properties() == ["rob", "1212", "first", "male"]
    assert not s1.is_amat()
    s1.add_subject(['computer science', "5"])
    s1.add_subject(['physics', "5"])
    assert s1.is_amat()
    s1.scientific_subjects()
    assert str(s1) == "rob,1212,first,male,math,5,computer science,5,physics,5"
    main()
