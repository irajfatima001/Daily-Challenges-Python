
import re
print("------Password Strength Checker------")

password = input("Enter your password:")

pass_length=len(password)

if pass_length < 6 :
    print("your password is weak! Try atleast 6 character.")
elif (pass_length >= 8 and
          re.search(r'[A-Z]', password) and 
          re.search(r'[a-z]', password) and 
          re.search(r'\d', password) and    
          re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):  
        print (" Strong Password! Great job! ")
else:
    print(" Your password is MODERATE! Try adding uppercase, numbers, and special characters.")    