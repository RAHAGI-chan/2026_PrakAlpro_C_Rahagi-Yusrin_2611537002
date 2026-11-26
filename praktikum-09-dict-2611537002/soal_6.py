schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

# 6a. Hari dengan mata kuliah terbanyak dan jumlahnya
if schedule:
    busiest_day, courses = max(schedule.items(), key=lambda item: len(item[1]))
    print(f"Busiest day: {busiest_day} ({len(courses)} courses)")

# 6b. Hitung jumlah hari munculnya mata kuliah yang diinput
course_query = input().strip()
day_count = sum(1 for courses in schedule.values() if course_query in courses)
print(f"{course_query}: {day_count} days")