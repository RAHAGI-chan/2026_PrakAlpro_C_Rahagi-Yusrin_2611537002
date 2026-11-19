number_of_rows = 4
seats_per_row = 5
# Write your code below

# 1. Buat denah 4 baris x 5 kursi dengan list terpisah tiap baris
seats = [["."] * seats_per_row for _ in range(number_of_rows)]

while True:
    # Tampilkan denah kursi
    for r in range(number_of_rows):
        row_display = " ".join(seats[r])
        print(f"Row {r + 1}: {row_display}")

    row_input = int(input("Row (0 to stop): "))
    if row_input == 0:
        break

    seat_input = int(input("Seat: "))

    # Cek apakah nomor baris atau nomor kursi di luar rentang (1..number_of_rows / 1..seats_per_row)
    if (
        row_input < 1
        or row_input > number_of_rows
        or seat_input < 1
        or seat_input > seats_per_row
    ):
        print("Invalid seat.")
        continue

    r_idx = row_input - 1
    s_idx = seat_input - 1

    # Cek apakah kursi sudah terisi ('X')
    if seats[r_idx][s_idx] == "X":
        print("Seat already taken.")
    else:
        seats[r_idx][s_idx] = "X"
        print("Seat booked.")

# Hitung total kursi yang terisi ('X')
taken_count = 0
for row in seats:
    for cell in row:
        if cell == "X":
            taken_count += 1

print(f"Seats taken: {taken_count}")