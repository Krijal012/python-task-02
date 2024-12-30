# How can you print "softwarica" 10 times?
# for i in range (10) :
#     print("softwarica")

# How can you find the sum of numbers in a list?
# lst = [1, 2, 3, 4]
# total = 0
# for num in lst:
#     total += num
# print("Sum of list:", total)

# How can you print each character of a string?
# string = "softwarica"
# for i in range (len(string)) :
#     print(string[i])

# How can you print only the integers from a mixed list?
# list = [1, "a", "b", 2, 3, 4]
# for item in list:
#     if isinstance(item, int):
#         print(item)

# How can you calculate the multiplication of all numbers in a list?
# list = [4, 5, 3, 2]
# result = 1
# for num in list:
#     result *= num
# print("Multiplication result:", result)

# How can you print the multiplication table of a number?
# number = 5
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")

# How can you reverse a list?
# list = [1, 2, 3, 4]
# rev_list = []
# for i in range(len(list) - 1, -1, -1):
#     rev_list.append(list[i])
# print("Reversed list:", rev_list)

# How can you add 1 to each number in a list?
# list = [1, 2, 3, 4]
# new_list = []
# for num in list:
#     new_list.append(num + 1)
# print("New list:", new_list)

# How can you print the first and last element of a list?
# list = [1, 2, 3, 4]
# for i in range(len(list)):
#     if i == 0 or i == len(list) - 1:
#         print(list[i])

# How can you print the first, second, and last element of a list?
# list = [1, 2, 3, 4]
# for i in range(len(list)):
#     if i == 0 or i == 1 or i == len(list) - 1:
#         print(list[i])

# How can you modify a list by replacing a specific element?
# list = [1, 2, 3, 4]
# new_list = []
# for i in range(len(list)):
#     if i == 1:
#         new_list.append("a")
#     else:
#         new_list.append(list[i])
# print("Modified list:", new_list)

# How can you separate odd and even numbers from a list?
# lst = [1, 2, 3, 4, 5]
# odd = []
# even = []
# for num in lst:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)
# print("Odd numbers:", odd)
# print("Even numbers:", even)

# How can you separate integers and strings from a mixed list?
# list = [1, 2, 3, "a", 4, 5, "b"]
# integers = []
# strings = []
# for item in list:
#     if isinstance(item, int):
#         integers.append(item)
#     elif isinstance(item, str):
#         strings.append(item)
# print("Integers:", integers)
# print("Strings:", strings)

# How can you separate integers and strings in a list of mixed data types?
# list = [1, 2, 3, 4, "a", "b"]
# int_types = []
# str_types = []
# for item in list:
#     if isinstance(item, int):
#         int_types.append(item)
#     elif isinstance(item, str):
#         str_types.append(item)
# print("Integer Types:", int_types)
# print("String Types:", str_types)

# How can you count the number of letters, digits, and spaces in a string?
# string = "Python Programming 123!"
# letters, digits, spaces = 0, 0, 0
# for char in string:
#     if char.isdigit():
#         digits += 1
#     elif char.isalpha():
#         letters += 1
#     elif char.isspace():
#         spaces += 1
# print("Letters:", letters, "Digits:", digits, "Spaces:", spaces)

# How can you validate the length of a username and password?
# username = input("Enter username: ")
# password = input("Enter password: ")

# is_valid_use = False
# is_valid_pass = False
# for _ in username:
#     if len(username) >= 5:
#         is_valid_use = True
#         break
# for _ in password:
#     if len(password) >= 8:
#         is_valid_pass = True
#         break
# if is_valid_use and is_valid_pass:
#     print("Valid credentials")
# else:
#     print("Invalid credentials")

# How can you check if a number is even or odd?
# num = int(input("Enter a number: "))
# for _ in range(1): 
#     if num % 2 == 0:
#         print(f"{num} is Even")
#     else:
#         print(f"{num} is Odd")

# How can you calculate the factorial of a number?
# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print("Factorial:", factorial)

# How can you print the multiplication table for multiple numbers?
# for num in range(1, 9):
#     print(f"Multiplication Table of {num}:")
#     for i in range(1, 11):
#         print(f"{num} x {i} = {num * i}")
#     print()

# How can you print the first two elements of a list?
# list = [1, 2, 3, 4]
# for i in range(len(list)):
#     if i < 2:
#         print(list[i])

# How can you sum the odd numbers between 1 and 10?
# start, end = 1, 10
# odd_sum = 0
# for num in range(start, end + 1):
#     if num % 2 != 0:
#         odd_sum += num
# print("Sum of odd numbers:", odd_sum)

# How can you sum the even numbers between 1 and 10?
# even_sum = 0
# for num in range(start, end + 1):
#     if num % 2 == 0:
#         even_sum += num
# print("Sum of even numbers:", even_sum)

# How can you count the number of spaces in a string?
# string = "Hello World. This is Binayak"
# space_count = 0
# for char in string:
#     if char.isspace():
#         space_count += 1
# print("Spaces:", space_count)

# How can you cube each number in a list?
# list = [1, 2, 3, 4]
# cubed_list = []
# for num in list:
#     cubed_list.append(num ** 3)
# print("Cubed list:", cubed_list)

# How can you reverse a string?
# a = "programming"
# reversed_string = ""
# for char in a:
#     reversed_string = char + reversed_string
# print("Reversed string:", reversed_string)

# How can you break out of a loop when a condition is met?
# for i in range(50):
#     if i > 7:
#         break
#     print(i)

# How can you print each character of a string?
# string = "hello"
# for char in string:
#     print(char)

# How can you greet each name in a list?
# a = ["ram", "shyam", 1, 2]
# for name in a:
#     if isinstance(name, str):
#         print(f"Hello! {name}")

# How can you add "Dr." to each name in a list?
# a = ["ram", "shyam"]
# new_list = []
# for item in a:
#     new_list.append(f"Dr.{item}")
# print(new_list)

# How can you square each number in a list?
# list = [1, 2, 3, 4]
# squared_list = []
# for num in list:
#     squared_list.append(num ** 2)
# print("Squared list:", squared_list)

#  How can we extract only the positive numbers from list?
# list1 = [111, 32, -9, -45, -17, 9, 85, -10]
# positive_numbers = []
# for num in list1:
#     if num > 0:
#         positive_numbers.append(num)
# print("Positive numbers:", positive_numbers)

# How can we print all the numbers except for 3 and 6 from list?
# list = [0, 1, 2, 3, 4, 5, 6]
# for num in list:
#     if num != 3 and num != 6:
#         print(num, end=" ")

# How can we get the types of each element in the list?
# list = [1, "hello", 3.5, True]
# type_list = []
# for item in lst:
#     type_list.append(type(item))
# print("\nType list:", type_list)

# How can we print numbers from 0 to 4 and then display "Done"?
# for i in range(5):
#     print(i)
# else:
#     print("Done")

# How can we print numbers from 105 to 6, decrementing by 7 each time?
# for num in range(105, 6, -7):
#     print(num, end=" ")

# Given the string string = "py;th* o:n ! ;py * t*h:o !n", how can we remove specific unwanted characters and spaces from it?
# bad_chars = [';', ':', '!', '*']
# string = "py;th* o:n ! ;py * t*h:o !n"
# good_string = ""
# for char in string:
#     if char not in bad_chars:
#         good_string += char
# good_string = good_string.replace(" ", "")
# print("\nCleaned string:", good_string)

# Given the list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], how can we count the number of even and odd numbers?
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = 0
# odd = 0
# for num in numbers:
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Even count:", even, "Odd count:", odd)

#  How can we find the sum of numbers between 3 and 100 that are divisible by 3 or 5?
# total = 0
# for num in range(3, 100):
#     if num % 3 == 0 or num % 5 == 0:
#         total += num
# print("Sum of multiples:", total)

# How can we calculate the sum of all even and odd numbers between 1 and 100?
# even, odd = 0, 0
# for num in range(1, 101):
#     if num % 2 == 0:
#         even += num
#     else:
#         odd += num
# print("Even sum:", even, "Odd sum:", odd)

# How can we check if the number 121 is a palindrome?
# num = 121
# rev_num = 0
# for digit in str(num):
#     rev_num = int(str(digit) + str(rev_num))
# if num == rev_num:
#     print(f"{num} is a palindrome")
# else:
#     print(f"{num} is not a palindrome")

# How can we check if the number 153 is an Armstrong number?
# num = 153
# sum = 0
# for digit in str(num):
#     sum += int(digit) ** 3
# if sum == num:
#     print(f"{num} is an Armstrong number")
# else:
#     print(f"{num} is not an Armstrong number")

# Given the string string = "python programming", how can we remove all vowels from it?
# string = "python programming"
# vowels = "aeiou"
# no_vowels = ""
# for char in string:
#     if char not in vowels:
#         no_vowels += char
# print("String without vowels:", no_vowels)

# How can we check if the number 28 is a perfect number?
# num = 28
# sum = 0
# for i in range(1, num):
#     if num % i == 0:
#         sum += i
# if sum == num:
#     print(f"{num} is a perfect number")
# else:
#     print(f"{num} is not a perfect number")

# How can we find the common elements between the lists list1 = [1, 2, 3, 4, 5] and list2 = [3, 4, 5, 6, 7]?
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# common_elements = []
# for item in list1:
#     if item in list2:
#         common_elements.append(item)
# print("Common elements:", common_elements)

# How can we check if the number 29 is a prime number?
# num = 29
# is_prime = True
# for i in range(2, num):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime and num > 1:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")