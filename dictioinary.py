# Modifying the dictionaries in a list
# Creating a mother list to house the puppies
puppies = []
# Making 100 new puppies.
for total_puppies in range(100):
    new_puppy = {'color': 'grey', 'speed': '10'}
    puppies.append(new_puppy)
for puppy in puppies[0:2]:
    if puppy['color'] == 'grey':
        puppy['color'] = 'black'
        puppy['speed'] = 12

for puppy in puppies[:5]:
    print(puppy)
    print('...')

print('The complete number of puppies is ' + str(len(puppies)))