def calculator(num1, num2, operator):

    if operator == "/" and num2 == 0: # Special case: Handle division by zero

        return "Error: Division by zero is not allowed"
    # execute calculations
    if operator == "+":
        result = num1 + num2
        print(f"The result is: {result}")
    elif operator == "-": 
        result = num1 - num2

    
    elif operator == "*":  
        result = num1 * num2
    elif operator == "/":  
        result = num1 / num2
    elif operator == "-":  
        result = num1 / num2
    elif operator == "%":  
        result = num1 % num2
    elif operator == ">":
        result = num1 > num2
    elif operator == ">=":
        result = num1 >= num2
    elif operator == "<":
        result = num1 < num2
    elif operator == "<=":
        result = num1 <= num2
    else:
    
        return "Invalid operator."  # If the operator is not recognized, return an error message

    return result

def max_of_three(num1, num2, num3):
    
    
    maximum = num1  # Initialize 'maximum' to num1, assuming it's the largest initially
    if num2 > maximum: # if num2 bigger then num1 return num2
        maximum = num2
    if num3 > maximum:  #if bigger than num2 return num3
        maximum = num3
    return maximum

def winning_numbers(user_list, winning_list):  # Calculate the number of matches between user_list and winning_list
    prize = 'No'
    
    match_count = len(set(user_list) & set(winning_list))
   # Determines the prize on the number of matches
    if match_count == 3:
        prize = "First"
    elif match_count == 2:
        prize = "Second"
    elif match_count == 1:
        prize = "Third"
    else:
        prize == "No"
    return prize

def sum_of_evens(min_value, max_value):
    
    total = 0  # Initialize the total sum to 0
    for num in range(min_value, max_value +1):  # Iterate through the range of numbers from min_value to max_value 

        if num % 2 == 0:  # Check if the current number is even

            total += num  # Add the even number to the total sum
    
    return total

def is_prime(num):
    
    output = True   # Assume the number is prime initially
     
    if num < 2:  # Numbers less than 2 are not prime

        return not output  # Flip output to False for numbers < 2

    for i in range(2, int(num**0.5) + 1): # Check divisors from 2 to the square root of the number
        if num % i == 0:  # If num is divisible by i, it's not prime
            return not output # Flip output to False and return
        
    return output

def are_anagrams(str1, str2):
   

    output = True  # Assume the strings are anagrams initially
     
   # Check if the sorted versions of the strings are different
    if sorted(str1) != sorted(str2):  
        return not output  # Flip output to False
   
   # Check if every letter in str1 exists in str2
    for letter in str1:  
        if letter not in str2:
            return not output  # Flip output to False if any letter is missing

    return output

def calculate_average(numbers):
   
   # Initialize the total sum to 0 and count to 0
    total_sum = 0
    count = 0
    
    # Iterate through each number in the numbers list
    for number in numbers:
        total_sum += number  # Add the current number to the total sum
        count += 1  # Increment the count by 1 for each number

    # If there are any numbers (count > 0), calculate the average
    if count > 0:
        average = total_sum / count
    else:
        average = 0  # If the list is empty (count == 0), return 0 to avoid division by zero


    return average

def calculate_weekly_pay(hours_worked):
    
    regular_rate = 12  # £12 per hour for up to 35 hours
    overtime_rate = 18  # £18 per hour for hours worked beyond 35 hours
    standard_hours = 35  # Threshold for regular pay

    # Calculates total pay, including regular pay for standard hours and overtime pay for hours beyond standard.
    if hours_worked <= standard_hours:
        total_pay = hours_worked * regular_rate
    else:
        regular_pay = standard_hours * regular_rate
        overtime_hours = hours_worked - standard_hours
        overtime_pay = overtime_hours * overtime_rate
        total_pay = regular_pay + overtime_pay



    return total_pay
    
def km_to_miles(kilometers):
    #Converts kilometers to miles using a conversion factor and rounds to 3 decimal places.
    conversion_factor = 0.62
    
    miles = round(kilometers * conversion_factor,3)

    return miles

def celsius_to_fahrenheit(celsius):
   # Converts Celsius to Fahrenheit 
   output = (celsius * 9/5) + 32

   return output

def annual_net_income(gross_salary):

    if gross_salary >= 45000:
        tax_rate = 0.50 # 0.50 = 50%
    elif gross_salary >= 30000:
        tax_rate = 0.30  # 0.30 = 30%
    else:
        tax_rate = 0.15  # 0.15 = 15%
    
    net_salary = gross_salary * (1 - tax_rate) #  Calculates net salary after applying tax rates based on gross salary.

    return net_salary

def letter_occurrence(input_string):

    
    count = 0
# Counts the occurrences of 'a' or 'A' in the input string.
    for char in input_string:
        if char == 'a' or char == 'A':
            count += 1
    
    return count

def fuel_cost(distance_miles):
#     # Constants
     MPG = 50  # Miles per gallon
     LITERS_PER_GALLON = 4.5
     PRICE_PER_LITER = 1.49  # Price in pounds per liter
#     continue function implementation here...
     
     # Calculate the total gallons used
     gallons_used = distance_miles / MPG
     
     # Convert gallons to liters
     liters_used = gallons_used * LITERS_PER_GALLON

     # Calculate total cost
     total_cost = liters_used * PRICE_PER_LITER

     return total_cost

def find_maximum_difference(a, b):
#     # Calculates the maximum difference between the max and min values of two lists.
     max1 = max(a)
     min1 = min(a)
     max2 = max(b)
     min2 = min(b)

     difference1 = max1 - min2
     difference2 = max2 - min1

     maximum = max(difference1, difference2)

     return maximum

def is_golden_number(n):
    boolean = False
#     # function implementation ...
    if n <= 0 or n >= 1000:
        return boolean
    
    # Checks if a number can be split into two factors whose product is divisible by 1000.
    for a in range(1,n):
        b = n - a
        if b > 0:
            if (a * b) % 1000 == 0:
                boolean = True
                break

    return boolean

def decrypt_cypher_text(encrypted_text, key):
#    # Decrypts a given text using a specified key by shifting ASCII values.
    if not isinstance(key, int) or key < 0:
        raise ValueError("key must be apositive integer.")
    decrypted_text = ""
    for char in encrypted_text:
        ascii_code =ord(char)

        new_ascii_code = ascii_code - key

        new_ascii_code = new_ascii_code % 256
        
        decrypted_char = chr(new_ascii_code)

        decrypted_text += decrypted_char

    return decrypted_text

