shortlist = [1,2,3,4,5]
x = sum(shortlist)
print(x)
len(x)
calculating the mean
def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s/N

if __name__ == '__main__':
    donations = [100,60,34,600,455,23,100]
    mean = calculate_mean(donations)
    N = len(donations)
    print('Mean donations over the last{0} days is {1}'.format(N,mean))


# calculating the frequency table
from collections import Counter
def frequency_table(numbers):
    table = Counter(numbers)
    print('number\tfrequency')
    for number in table.most_common():
        print('{0}\t{1}'.format(number[0],number[1]))
if __name__ == '__main__':
    scores = [2,4,3,2,6,5,66,3,2,5,66,3,2,4,2]
    frequency_table(scores)