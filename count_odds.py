# Add the odd numbers between 0 and 5000

# Result variable that will add sum of odd numbers.
result = 0

# Creates num variable that will iteriate in a while loop.
num = 0

# Asks user to input number to add the sum of and converts it to an integer.
number_to_check = input("please input a number greater than 1: ")
number_to_check = int(number_to_check)

while num <= number_to_check:
    is_odd = num % 2 != 0
    if is_odd:
          #print(num)
       result += num
    num += 1







print(result)