# Chapter 11 p103, printing only the value in Dictionary
english_language = {
    'Fred': '60',
    'Annie': '56',
    'Ann': '45'
}
complainants = ['Fred', 'Johnson']
print('print the dictionary: ')
print(english_language)

print('Adding new entries into a dictionary: ')
english_language['Dream'] = '60'
english_language['Lucy'] = '70'
print(english_language)

print('Building a dictionary from the scratch: ')
student_1 = {}
student_2 = {}
student_3 = {}
student_1['English_language'] = '60'
student_1['Math'] = '70'
student_2['English_language'] = '65'
student_2['Math'] = '75'
student_3['English_language'] = '69'
student_3['Math'] = '79'
print(student_1)
print(student_2)
print(student_3)
print('Using the for loop in a dictionary print items: ')
for student, score in english_language.items():
    print('students: ' + student)
    print('score: ' + score)

print('Making the for loop work with only Keys Name: ')
for student in english_language.keys():
    print(student.title())

print('These are the scores made by the students.')
for score in english_language.values():
    print(score)
