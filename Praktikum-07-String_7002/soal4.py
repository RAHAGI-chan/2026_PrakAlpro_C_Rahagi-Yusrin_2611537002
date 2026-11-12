# Name: Rahagi Yusrin
# NIM: 2611537002
# Question 4

phone = "081234567890"
masked = phone[:4] + "*" * (len (phone) - 7) + phone [-3:]
print(masked)
