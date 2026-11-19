menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below

# 1. Baca data dengan nested loop (baris = hari, kolom = menu)
for day in range(1, number_of_days + 1):
    row = []
    for menu in menus:
        qty = int(input(f"Day {day}, {menu}: "))
        row.append(qty)
    sales.append(row)

# 2. Cetak total porsi setiap hari (traversal per baris)
print("Total per day:")
for day_idx, row in enumerate(sales, start=1):
    day_total = 0
    for qty in row:
        day_total += qty
    print(f"Day {day_idx}: {day_total}")

# 3. Hitung total setiap menu (traversal per kolom) -> list of tuple (nama_menu, total)
menu_totals = []
for col_idx, menu in enumerate(menus):
    menu_total = 0
    for row_idx in range(number_of_days):
        menu_total += sales[row_idx][col_idx]
    menu_totals.append((menu, menu_total))

print(f"Total per menu: {menu_totals}")

# 4. Cari menu terlaris (jika sama, pilih yang muncul lebih dulu)
best_menu = menu_totals[0][0]
best_total = menu_totals[0][1]

for name, total in menu_totals:
    if total > best_total:
        best_total = total
        best_menu = name

print(f"Best seller: {best_menu} ({best_total})")