# This module contains the program for storing students' information.
class Students:
    def __init__(self, name, subject, score):
        self.name = name
        self.subject = subject
        self.score = score

    def fetch_students_info(self):
        full_info = self.name.title() + ' scored ' + str(self.score) + ' in ' + self.subject.title() + '.'
        return full_info


class NationalDetails():
    def __init__(self, nationality='European'):
        self.nationality = nationality

    def describe_national_details(self):
        print('This students nationality is ' + self.nationality + '.')

    def get_scholarship(self):
        if self.nationality == 'European':
            scholarship = 'full'
        elif self.nationality != 'European':
            scholarship = 'nil'
        statement = 'This student is on ' + scholarship + ' scholarship.'
        print(statement)


class ForeignStudent(Students):
    def __init__(self, name, subject, score):
        super().__init__(name, subject, score)
        self.NationalDetails = NationalDetails()
