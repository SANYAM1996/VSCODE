# find the factors of the integer
# def factor (b):
#     for i in range(1,b+1):
#         if b%i == 0:
#             print(i)
# if __name__ == '__main__':
    
#     b = input('your number please')
#     b = float(b)
#     if b > 0 and b.is_integer():
#         factor(int(b))
#     else:
#         print('enter the positive integer')

# creating multiplication table by function and using.format
# def multi_table(a):
#     for i in range (1, 11):
#         print('{0} x {1} = {2}'.format(a, i, a*i))
# if __name__ == "__main__":
#     a = input('enter the number: ')
#     multi_table(float(a))
# '''
'''Unit converter: Miles and Kilometers
'''
def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609
    print('Distance in miles: {0}'.format(miles))
def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609
    print('Distance in kilometers: {0}'.format(km))
if __name__ == '__main__':

    print_menu()
    choice = input('Which conversion would you like to do?: ')
    if choice == '1':

        km_miles()
    if choice == '2':

        miles_km()