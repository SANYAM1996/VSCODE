# find the factors of the integer
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