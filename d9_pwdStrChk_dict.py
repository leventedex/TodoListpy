password = input("Enter your password: ")
result = {}

#check if the password is at least 8 characters
if len(password) < 8:
    result['length'] = False
else:
    result["length"] = True

#check if the password has at least one digit
digit = False
for char in password:
    if char.isdigit():
        digit = True
result["digit"] = digit

#check if the password has at least one uppercase letter
upper = False
for char in password:
    if char.isupper():
        upper = True
result["upper_case"] = upper

print(result)
if all(result.values()):
    print("Password is strong!")
else:
    print("Password is weak!")