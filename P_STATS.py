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

# finding the rangae
def find_range(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    # find the range
    r = highest - lowest
    return lowest,highest,r
if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    lowest,highest,r = find_range(donations)
    print('lowest:{0} highest :{1} range:{2}'.format(low,highest,r))


