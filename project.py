import random
import string

pass_len = int(input("Please Enter the length of your Password: "))
charValues = string.ascii_letters + string.digits + string.punctuation

# List comprehension [function for i in range(n)]

password = "".join([random.choice(charValues) for i in range(pass_len)])

# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)

print("Your Random password is :", password)
