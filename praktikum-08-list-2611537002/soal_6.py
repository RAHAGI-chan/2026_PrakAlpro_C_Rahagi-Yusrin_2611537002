LAST_DIGIT = 2  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below

for day in range(1, 8):
    amount = int(input(f"Day {day}: "))
    expenses.append(amount)

total = 0
for exp in expenses:
    total += exp

average = total / len(expenses)

highest_val = expenses[0]
highest_day = 1
for i in range(1, len(expenses)):
    if expenses[i] > highest_val:
        highest_val = expenses[i]
        highest_day = i + 1

days_above_limit = 0
for exp in expenses:
    if exp > daily_limit:
        days_above_limit += 1

print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest_val})")
print(f"Days above limit: {days_above_limit}")