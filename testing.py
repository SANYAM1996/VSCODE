# importing function from the name_function .py files
from name_function.py import get_name
print('enter q at any time to quit')
while True:
    first = ('enter your first name')
    if first == 'q':
        break
    last = ('enter your last name')
    if last == 'q':
        break
    formatted_name = get_name(first,last)
    print('neatly formatted name :' + formatted_name.title())
