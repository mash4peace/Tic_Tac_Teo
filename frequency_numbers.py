#Frequrncy table for a list of numbers
from collections import Counter
def frequency_table(numbers):
    table = Counter(numbers)
    number_frq = table.most_common()
    number_frq.sort()
    print("Number\tFrequency")
    for num in number_frq:
        print('{0}\t{1}'.format(num[0],num[1]))
if __name__ == '__main__':
    scores = [7,8,9,2,10,9,9,9,9,4,5,6,1,5,6,7,8,6,1,10]
    frequency_table(scores)
