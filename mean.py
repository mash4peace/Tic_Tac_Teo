#This program will calculate Mean of numbers.
def calculate_mean(numbers):
    sum_of_numbers= sum(numbers)
    num_length= len(numbers)
    mean = sum_of_numbers/num_length
    return mean
if __name__ == '__main__':
    donation = [100, 60, 70, 900, 100, 200, 500,500, 503, 600, 1000,1200 ]
    mean = calculate_mean(donation)
    N = len(donation)
    print("Mean donation over the last 
    
    
#The output of the program is    
#Mean donation over the last 12 days is 477.75
