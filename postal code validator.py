import re 

pat = r'^\d{6}$'

postal_code = input("Please enter your postal code: ")

if re.match(pat, postal_code):
    print("This is a valid Singapore postal code.")
else: 
    print("This is an invalid Singapore posal code. Please enter a 6-digit number.")