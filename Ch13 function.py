def welcome(username):
    print('Welcome ' + username.title() + 'to my coding world!')


welcome('dream ')
welcome('JASON')
welcome('lily')
welcome('lucy')


def describe_institution(institution_type, institution_name):
    """Compose a short sentence about institution"""
    print('The name of my' + institution_type + 'is' + institution_name.upper() + '.')


describe_institution(' University ', ' UNO')
describe_institution(institution_name=' UNO', institution_type=' University ')


def bye_bye(name):
    """Compose a byebye sentence"""
    print('Bye bye my friends ' + name.title() + '!')


bye_bye('Qinzi')


def pupil_poem(pupil_name, pupil_age, pupil_class, favorite_teacher):
    """Print a little poem with pupil's details in it."""
    print('My name is ' + pupil_name.title())
    print('I am ' + str(pupil_age) + ' years old.')
    print('I am in class ' + str(pupil_class) + '.')
    print('My favorite teacher is ' + favorite_teacher.title() + '.')
    print('I am proud of him.\n')


pupil_poem('Jane', 8, 4, 'Ferguson')
pupil_poem('Angel', 7, 4, 'Alex')
pupil_poem('Smith', 6, 3, 'Hills')
