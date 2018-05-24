#Calculating the mode when the list of numbers may have multiple modes
import collections
from collections import Counter
def calculate_mode(numbers):
    c = Counter(numbers)
    numb_frq = c.most_common()
    max_count = numb_frq[0][1]
    modes = []
    for num in numb_frq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes
if __name__ == '__main__':
    scores = [5,5,5,4,4,4,9,1,3]
    modes = calculate_mode(scores)
    print("The mode(s) of the list of numbers are: ")
    for mode in modes:
        print(mode)

