# Name: Rahagi Yusrin
# NIM: 2611537002
# Question 5

# A
username = input("Username: ")

limit = len(username)
if limit < 5:
    print("Invalid: at least 5 characters")

for char in username:
    if char in username[0] != "qwertyuioplkjhgfdsazxcvbnm":
        print("Invalid: Must start with a letter")
    elif char in username != "1234567890poiuytrewqasdfghjlmnbvcxz":
        print("Invalid: Letters and digit only")
    else:
        print("VALID")
print()        




# Check the rules in a safe order and print the first rule that fails.
# Messages:
#   "Invalid: at least 5 characters"
#   "Invalid: letters and digits only"
#   "Invalid: must start with a letter"
#   "Valid"

# B

