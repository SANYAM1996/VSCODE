# # find the factors of the integer
def factor (b):
    for i in range(1,b+1):
        if b%i == 0:
            print(i)
if __name__ == '__main__':

    b = input('your number please')
    b = float(b)
    if b > 0 and b.is_integer():
        factor(int(b))
    else:
        print('enter the positive integer')
#
# # creating multiplication table by function and using.format
def multi_table(a):
    for i in range (1, 11):
        print('{0} x {1} = {2}'.format(a, i, a*i))
if __name__ == "__main__":
    a = input('enter the number: ')
    multi_table(float(a))
# Unit converter: Miles and Kilometers

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

# currency converter
def print_menu():
    print('1 Euro to rupees')
    print('2 Rupees to euro')
    print('3 Dollar to rupees')
    print('4 rupees to dollar')
def euro_rup():
    euro = float(input('enter the currency in euro :'))
    rupees = euro * 80
    print('currency in rupees ₹ : {0}'.format(rupees))
def rup_euro():
    rupees = float(input('enter the currency in ruppes ₹: '))
    euro = rupees/80
    print('currency in euro :{0}'.format(euro))
def d_r():
    dollar = float(input('enter the currency in dollar $: '))
    rupees = dollar * 66
    print('currency in rupees is ₹ :{0}'.format(rupees))
def r_d():
    rupees = float(input('enter the currency in the rupees ₹:'))
    dollar = rupees/66
    print('currency in dollar is ${0}'.format(dollar))
if __name__ == '__main__':

    print_menu()
    choice = input('which conversion would you like to do?:')
    if choice == '1':

        euro_rup()
    if choice == '2':
        rup_euro()
    if choice == '3':
        d_r()
    if choice == '4':
        r_d()
#
# # quadratic equation root calculator
def roots(a,b,c):
    D = (b*b - 4*a*c)**0.5
    x_1 = (-b + D)/(2*a)
    x_2 = (-b - D)/(2*a)

    print('x1 : {0}'.format(x_1))
    print('x2 : {0}'.format(x_2))
if __name__ == "__main__":

    a = (input('enter a :'))
    b = (input('enter b :'))
    c = (input('enter c :'))
    roots = (float(a),float(b),float(c))

# fraction calculator
from fractions import fraction
def  add(a,b):
    print('result of addition:{0}'.format(a+b))
if __name__ = '__main__':
    a = fraction(input('enter the first fraction'))
    b = fraction(input('enter the second fraction'))
    op = input('operation to perform - add,subtract,division,multiply: ')
    if op == 'add':
        add(a,b)

# even odd vending machine
def even_odd_vend(num):
    if (num%2) == 0:
        print('even')
    else:
        print('odd')
    count = 1
    while count <=9:
        num+=2
        print(num)
        count+=1
if __name__ == '__main__':
    try:
        num = float(input('enter the number'))
         if num.is_integer():
            even_odd_vend(int(num))
        else:
            print('Please enter an integer')
    except ValueError:
        print('Please enter a number')
# multiplication of table with exit function
def multi_table(a):
    for i in range(1,11):
        print('{0} * {1} = {2}'.format(a,i,a*i))
if __name__ =='__main__':
    while True:
        a = input('enter the number: ')
        multi_table(float(a))
        answer = input('do you want to exit? (y) for yes')
        if answer == 'y':
            break
# visualizing the graphs
import matplotlib.pyplot as plt
nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]
months = range(1,13)
plt.legend([2000,2006,2012])
plt.plot(months,nyc_temp_2000,months,nyc_temp_2006,months,nyc_temp_2012,marker = 'o')
from pylab import legend,title,xlabel,ylabel
legend([2000,2006,2012])
title('average monthly temperature in NYC')
xlabel('month')
ylabel('temperature')
plt.show()

# plotting above graph with function
import matplotlib.pyplot as plt
def make_graph():
    nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
    nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
    nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]
    plt.plot(nyc_temp_2000,nyc_temp_2006,nyc_temp_2012)
    plt.show()
if __name__ == '__main__':
    make_graph()

# temperature varying graph
def plot_forecast():
    time_of_day = ['4 AM', '7 AM', '10 AM', '1 PM', '4 PM', '7PM', '10 PM']
    forecast_temp = [71, 70, 74, 80, 82, 81, 76]
    time_interval = range(1, len(time_of_day) + 1)
    plt.xlabel('time of day')
    plt.ylabel('forecast')
    plt.plot(time_interval, forecast_temp, 'o-')
    plt.xticks(time_interval, time_of_day)
    plt.title('temperature NYC')
    plt.show()
if __name__ == '__main__':
    plot_forecast()

    

