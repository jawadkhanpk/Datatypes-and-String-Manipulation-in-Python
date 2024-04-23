# Python program that adds 2-digit number entered by a user:
# E.g. if input= 25, then output should be: 2 + 5 =7

two_digit_number = input("Type a two digit number: ")

first_digit_number = two_digit_number[0]
second_digit_number = two_digit_number[1]

result = int(first_digit_number) + int(second_digit_number)

print(result)