class Students:
    def __init__(self, name, subject, score):
        self.name = name
        self.subject = subject
        self.score = score
        self.bonus = 5  # attributes with a default value

    def fetch_students_info(self):
        full_info = self.name.title() + ' scored ' + str(self.score) + ' in ' + self.subject.title() + '.'
        return full_info

    def general_bonus(self):
        print(self.name + ' also has a bonus of ' + str(self.bonus) + ' points. ')

    def update_score(self, final):  # Modifying the value of an attribute by using a method.
        self.score = final

    def total_points(self, total):
        self.score += total


# Converting Instances to Attributes
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
    def __init__(self, name, subject, score, year):
        super().__init__(name, subject, score)
        self.graduationYear = year
        self.NationalDetails = NationalDetails()


s2 = ForeignStudent('Paul', 'Math', 80, 2018)
print(s2.fetch_students_info() + ' Graduation year is ' + str(s2.graduationYear))
s2.NationalDetails.describe_national_details()
s2.NationalDetails.get_scholarship()

