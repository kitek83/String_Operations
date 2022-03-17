file_name = input('Enter file name.')
if file_name.endswith('.txt'):
    print('This is the name of text file')
elif file_name.endswith('.py'):
    print('This is python file')
elif file_name.endswith('.doc'):
    print('This is word document')
else:
    print('The file is unknown origin')