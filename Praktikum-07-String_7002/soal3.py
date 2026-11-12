# Name: Rahagi Yusrin
# NIM: 2611537002
# Question 3

# A
text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

# B

text = "Rahagi Yusrin"
count = 0
for char in text:
    if char in "Aaiueo":
        count = count + 1
print("Vowels:", count)
