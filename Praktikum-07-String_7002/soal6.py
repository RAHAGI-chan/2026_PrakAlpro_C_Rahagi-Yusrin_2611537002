# Name: Rahagi Yusrin
# NIM: 2611537002
# Question 6

first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())


full_name = "  Siti Aisyah  "
nim = "2610511023"

# 1. Remove leading and trailing spaces
cleaned_name = full_name.strip()

# 2. Find the position of the first space (returns -1 if not found)
space_index = cleaned_name.find(" ")

# 3. Extract the first name based on whether a space exists
if space_index == -1:
    first_name = cleaned_name
else:
    first_name = cleaned_name[:space_index]

# 4. Convert the first name to lowercase
first_name_lower = first_name.lower()

# 5. Extract the last 3 digits of the NIM
last_three_nim = nim[-3:]

# 6. Build and print the username
username = first_name_lower + last_three_nim
print(username)  # Output: siti023

# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().
