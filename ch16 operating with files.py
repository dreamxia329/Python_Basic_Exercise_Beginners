file_location = '/Users/dreamxia/Downloads/2022 Fall /CSCI2410-850 Intro To Python Data Analytics/test.txt'
with open(file_location) as file_output:
    contents = file_output.read()
    output = contents.replace('Smith', 'Henry')
    print(output)


file_name = 'experimental.txt'
with open(file_name, 'w') as file_output2:
    file_output2.write('Nothing serious going on here.\n')
    file_output2.write('Just testing with this code.\n')
with open(file_name, 'a') as file_output2:
    file_output2.write('Appending information test.\n')
with open(file_name, 'r') as file_output3:
    contents = file_output3.read()
    print(contents)
