class Boy:
    """This is a step towards modeling a class of boys."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(self.name.title() + ' is now running.')

    def jumping(self):
        print(self.name.title() + ' is now jumping')


boy_1 = Boy('Tom', 8)

print(boy_1.name)
print(boy_1.age)

print("The first boys name is " + boy_1.name.title() + ".")
print('He is ' + str(boy_1.age) + ' years old.')
boy_1.jumping()


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


s1 = Students('Jame', 'English', '100')
s1.update_score(95)
s1.bonus = 3
s1.general_bonus()
s1.total_points(3)
print(s1.fetch_students_info())

