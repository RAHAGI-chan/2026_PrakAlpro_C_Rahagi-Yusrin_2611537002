import tkinter as tk
from tkinter import ttk
from collections import Counter

# ==========================================
# 1. DATABASE LENGKAP
# ==========================================

DATABASE_COUNTER = {
    # --- ASSASSIN ---
    "Aamon": ["Saber", "Chou", "Franco", "Eudora"],
    "Benedetta": ["Minsitthar", "Khufra", "Phoveus", "Saber", "Ruby"],
    "Fanny": ["Khufra", "Franco", "Saber", "Chou", "Minsitthar", "Moskov", "Ruby"],
    "Gusion": ["Ruby", "Chou", "Khufra", "Minsitthar", "Saber"],
    "Hanzo": ["Natalia", "Ling", "Fanny", "Aldous", "Helcurt"],
    "Hayabusa": ["Saber", "Chou", "Kaja", "Franco", "Ruby"],
    "Helcurt": ["Hylos", "Belerick", "Gatotkaca", "Tigreal"],
    "Joy": ["Minsitthar", "Franco", "Kaja", "Phoveus"],
    "Karina": ["X.Borg", "Lylia", "Franco", "Chou"],
    "Lancelot": ["Khufra", "Chou", "Phoveus", "Ruby", "Minsitthar"],
    "Ling": ["Khufra", "Saber", "Ruby", "Moskov", "Minsitthar", "Franco"],
    "Natalia": ["Rafaela", "Aldous", "Hylos", "Belerick", "Yi Sun-shin"],
    "Nolan": ["Khufra", "Franco", "Kaja", "Chou"],
    "Saber": ["Argus", "Gatotkaca", "Chou"],
    "Selena": ["Diggie", "Khufra", "Kagura", "Chou"],

    # --- FIGHTER ---
    "Aldous": ["Chou", "Valir", "Akai", "Lylia"],
    "Alpha": ["Baxia", "Valir", "Chou"],
    "Alucard": ["Baxia", "Khufra", "Valir"],
    "Argus": ["Valir", "Akai", "Franco", "Jawhead"],
    "Arlott": ["Minsitthar", "Khufra", "Phoveus", "Franco"],
    "Aulus": ["Valir", "Belerick", "Chou"],
    "Badang": ["Chou", "Khufra", "Valir", "Phoveus"],
    "Balmond": ["Baxia", "Valir", "Karrie", "Dyrroth"],
    "Bane": ["Chou", "Valir", "Karrie"],
    "Barats": ["Karrie", "Claude", "Valir", "Baxia"],
    "Chou": ["Barats", "Paquito", "Yu Zhong", "Gatotkaca"],
    "Cici": ["Baxia", "Valir", "Minsitthar"],
    "Dyrroth": ["Terizla", "Gatotkaca", "Argus", "Chou"],
    "Freya": ["Baxia", "Minsitthar", "Valir", "Esmeralda"],
    "Guinevere": ["Helcurt", "Chou", "Minsitthar", "Kaja"],
    "Hilda": ["Valir", "Karrie", "Dyrroth", "Baxia"],
    "Jawhead": ["Valir", "Karrie", "Diggie"],
    "Julian": ["Chou", "Saber", "Phoveus"],
    "Khaleed": ["Baxia", "Valir", "Chou"],
    "Lapu-Lapu": ["Chou", "Franco", "Kaja"],
    "Leomord": ["Baxia", "Khufra", "Minsitthar"],
    "Martis": ["Phoveus", "Gatotkaca", "Argus", "Valir"],
    "Minsitthar": ["Diggie", "Chou", "Valir", "Akai"],
    "Paquito": ["Phoveus", "Chou", "Khufra"],
    "Phoveus": ["Esmeralda", "Karrie", "Lunox", "Dyrroth"],
    "Roger": ["Baxia", "Gatotkaca", "Belerick", "Khufra"],
    "Ruby": ["Baxia", "Valir", "Phoveus"],
    "Silvanna": ["Diggie", "Chou", "Kadita", "Akai"],
    "Sun": ["X.Borg", "Balmond", "Odette", "Ruby"],
    "Terizla": ["Valir", "Karrie", "Lunox", "X.Borg"],
    "Thamuz": ["Baxia", "Karrie", "Valir", "Dyrroth"],
    "X.Borg": ["Kimmy", "Karrie", "Esmeralda", "Silvanna"],
    "Yin": ["Argus", "Gatotkaca", "Chou", "Valir"],
    "Yu Zhong": ["Baxia", "Karrie", "Dyrroth", "Valir"],
    "Zilong": ["Khufra", "Gatotkaca", "Belerick", "Hylos"],

    # --- MAGE ---
    "Alice": ["Baxia", "Karrie", "Lunox", "Valir"],
    "Aurora": ["Chou", "Saber", "Kaja"],
    "Cecilion": ["Aldous", "Natalia", "Chou", "Saber"],
    "Chang'e": ["Lolita", "Baxia", "Chou"],
    "Cyclops": ["Chou", "Saber", "Lancelot"],
    "Esmeralda": ["Baxia", "Karrie", "Lunox", "Valir"],
    "Eudora": ["Chou", "Saber", "Natalia"],
    "Faramis": ["Valentina", "Yin", "Akai"],
    "Gord": ["Chou", "Ling", "Fanny", "Natalia"],
    "Harith": ["Khufra", "Baxia", "Esmeralda", "Minsitthar"],
    "Harley": ["Chou", "Natalia", "Saber"],
    "Kadita": ["Chou", "Kaja", "Franco"],
    "Kagura": ["Chou", "Kaja", "Saber"],
    "Kimmy": ["Belerick", "Lolita", "Chou"],
    "Lunox": ["Chou", "Natalia", "Saber"],
    "Luo Yi": ["Chou", "Saber", "Natalia"],
    "Lylia": ["Chou", "Saber", "Khufra"],
    "Nana": ["Chou", "Natalia", "Saber"],
    "Novaria": ["Natalia", "Aldous", "Ling", "Fanny"],
    "Odette": ["Franco", "Chou", "Kaja", "Jawhead"],
    "Pharsa": ["Chou", "Khufra", "Aldous", "Natalia"],
    "Vale": ["Chou", "Saber", "Natalia"],
    "Valentina": ["Baxia", "Chou", "Saber"],
    "Valir": ["Baxia", "Chou", "Lancelot", "Ling"],
    "Vexana": ["Chou", "Saber", "Natalia"],
    "Yve": ["Franco", "Kaja", "Chou", "Aldous"],
    "Zhask": ["Claude", "Saber", "Chou"],

    # --- MARKSMAN ---
    "Beatrix": ["Belerick", "Natalia", "Chou", "Saber"],
    "Brody": ["Chou", "Natalia", "Saber"],
    "Bruno": ["Belerick", "Chou", "Saber"],
    "Claude": ["Belerick", "Chou", "Khufra"],
    "Clint": ["Chou", "Natalia", "Saber"],
    "Granger": ["Chou", "Ling", "Saber"],
    "Hanabi": ["Belerick", "Gatotkaca", "Chou"],
    "Irithel": ["Belerick", "Chou", "Saber"],
    "Ixia": ["Franco", "Chou", "Natalia", "Khufra"],
    "Karrie": ["Chou", "Natalia", "Saber"],
    "Layla": ["Natalia", "Ling", "Fanny", "Aldous"],
    "Lesley": ["Natalia", "Aldous", "Saber"],
    "Melissa": ["Belerick", "Franco", "Chou"],
    "Miya": ["Belerick", "Chou", "Gatotkaca"],
    "Moskov": ["Belerick", "Eudora", "Chou"],
    "Natan": ["Belerick", "Chou", "Saber"],
    "Popol and Kupa": ["Carmilla", "Hanabi", "Claude"],
    "Wanwan": ["Khufra", "Phoveus", "Franco", "Minsitthar"],
    "Yi Sun-shin": ["Chou", "Natalia", "Saber"],

    # --- TANK / SUPPORT ---
    "Akai": ["Diggie", "Valir", "Karrie"],
    "Angela": ["Baxia", "Chou", "Saber"],
    "Atlas": ["Diggie", "Valir", "Chou"],
    "Baxia": ["Valir", "Karrie", "Lunox"],
    "Belerick": ["Karrie", "Lunox", "Dyrroth", "X.Borg"],
    "Carmilla": ["Diggie", "Valir"],
    "Diggie": ["Hilda", "Natalia", "Mathilda"],
    "Edith": ["Karrie", "Lunox", "Valir", "Dyrroth"],
    "Estes": ["Baxia", "Luo Yi", "Atlas", "Carmilla"],
    "Floryn": ["Baxia", "Chou", "Natalia"],
    "Franco": ["Diggie", "Minsitthar", "Karrie"],
    "Gatotkaca": ["Karrie", "Lunox", "Valir", "Diggie"],
    "Gloo": ["Vexana", "Faramis", "Karrie", "Valir"],
    "Grock": ["Valir", "Karrie", "Lunox", "X.Borg"],
    "Hylos": ["Karrie", "Valir", "Lunox", "Baxia"],
    "Johnson": ["Diggie", "Grock", "Karrie", "Baxia"],
    "Khufra": ["Valir", "Diggie", "Karrie", "Franco"],
    "Lolita": ["Khufra", "Franco", "Grock"],
    "Mathilda": ["Khufra", "Minsitthar", "Franco"],
    "Minotaur": ["Diggie", "Valir", "Karrie"],
    "Rafaela": ["Chou", "Natalia", "Baxia"],
    "Tigreal": ["Diggie", "Akai", "Valir"]
}

# Kamus Pemetaan Role Hero (Sangat penting agar filter berdasarkan role berfungsi)
HERO_ROLES = {
    "Saber": ["Jungle", "Roam"],
    "Ling": ["Jungle"],
    "Fanny": ["Jungle"],
    "Helcurt": ["Jungle", "Roam"],
    "Lancelot": ["Jungle"],
    "Aldous": ["Jungle", "Exp Lane"],
    "Baxia": ["Jungle", "Roam"],
    "Akai": ["Jungle", "Roam", "Exp Lane"],
    "Balmond": ["Jungle", "Exp Lane"],
    "Dyrroth": ["Jungle", "Exp Lane"],
    "Barats": ["Jungle", "Exp Lane"],
    "Khufra": ["Roam"],
    "Franco": ["Roam"],
    "Chou": ["Roam", "Exp Lane"],
    "Minsitthar": ["Roam", "Exp Lane"],
    "Diggie": ["Roam", "Mid Lane"],
    "Kaja": ["Roam", "Exp Lane", "Mid Lane"],
    "Belerick": ["Roam", "Exp Lane"],
    "Gatotkaca": ["Roam", "Exp Lane"],
    "Hylos": ["Roam", "Jungle"],
    "Tigreal": ["Roam"],
    "Atlas": ["Roam"],
    "Lolita": ["Roam"],
    "Carmilla": ["Roam", "Jungle"],
    "Rafaela": ["Roam"],
    "Mathilda": ["Roam", "Mid Lane"],
    "Ruby": ["Exp Lane", "Roam"],
    "Phoveus": ["Exp Lane"],
    "Terizla": ["Exp Lane"],
    "X.Borg": ["Exp Lane", "Jungle"],
    "Argus": ["Exp Lane"],
    "Jawhead": ["Exp Lane", "Roam", "Jungle"],
    "Silvanna": ["Exp Lane", "Jungle"],
    "Esmeralda": ["Exp Lane", "Mid Lane", "Jungle"],
    "Yu Zhong": ["Exp Lane"],
    "Hilda": ["Exp Lane", "Roam"],
    "Valir": ["Mid Lane", "Roam"],
    "Eudora": ["Mid Lane"],
    "Lylia": ["Mid Lane"],
    "Kagura": ["Mid Lane"],
    "Lunox": ["Mid Lane", "Jungle"],
    "Kadita": ["Mid Lane", "Roam"],
    "Valentina": ["Mid Lane", "Exp Lane"],
    "Luo Yi": ["Mid Lane"],
    "Faramis": ["Mid Lane", "Roam"],
    "Vexana": ["Mid Lane"],
    "Karrie": ["Gold Lane", "Jungle"],
    "Claude": ["Gold Lane"],
    "Moskov": ["Gold Lane"],
    "Natalia": ["Roam", "Jungle"],
    "Yi Sun-shin": ["Jungle", "Gold Lane"],
    "Hanabi": ["Gold Lane"]
}

DATABASE_BUILD = {
    # ROAM / TANK
    "Khufra": ["Tough Boots", "Dominance Ice", "Athena's Shield", "Immortality", "Antique Cuirass", "Radiant Armor"],
    "Franco": ["Magic Shoes", "Dominance Ice", "Athena's Shield", "Antique Cuirass", "Immortality", "Radiant Armor"],
    "Baxia": ["Tough Boots", "Dominance Ice", "Cursed Helmet", "Radiant Armor", "Antique Cuirass", "Immortality"],
    "Belerick": ["Warrior Boots", "Dominance Ice", "Blade Armor", "Oracle", "Antique Cuirass", "Immortality"],
    "Gatotkaca": ["Warrior Boots", "Concentrated Energy", "Dominance Ice", "Blade Armor", "Athena's Shield", "Immortality"],
    "Minsitthar": ["Warrior Boots", "Corrosion Scythe", "Demon Hunter Sword", "Dominance Ice", "Athena's Shield", "Immortality"],
    "Diggie": ["Magic Shoes", "Fleeting Time", "Necklace of Durance", "Dominance Ice", "Athena's Shield", "Immortality"],
    "Akai": ["Tough Boots", "Cursed Helmet", "Dominance Ice", "Radiant Armor", "Antique Cuirass", "Immortality"],
    "Kaja": ["Magic Shoes", "Fleeting Time", "Dominance Ice", "Athena's Shield", "Antique Cuirass", "Immortality"],

    # EXP LANE
    "Chou": ["Warrior Boots", "Blade of the Heptaseas", "Hunter Strike", "Malefic Roar", "Blade of Despair", "Immortality"],
    "Phoveus": ["Demon Shoes", "Clock of Destiny", "Lightning Truncheon", "Holy Crystal", "Divine Glaive", "Blood Wings"],
    "Ruby": ["Tough Boots", "Bloodlust Axe", "Dominance Ice", "Hunter Strike", "Oracle", "Immortality"],
    "Terizla": ["Warrior Boots", "Bloodlust Axe", "Dominance Ice", "Hunter Strike", "Antique Cuirass", "Immortality"],
    "X.Borg": ["Magic Shoes", "Bloodlust Axe", "Ice Queen Wand", "Immortality", "Hunter Strike", "Blade of Despair"],
    "Dyrroth": ["Warrior Boots", "Hunter Strike", "Dominance Ice", "Malefic Roar", "Antique Cuirass", "Immortality"],
    "Aldous": ["Warrior Boots", "Thunder Belt", "Brute Force Breastplate", "Malefic Roar", "Athena's Shield", "Immortality"],

    # JUNGLE / ASSASSIN
    "Saber": ["Magic Shoes", "Hunter Strike", "Blade of the Heptaseas", "Malefic Roar", "Blade of Despair", "Immortality"],
    "Natalia": ["Rapid Boots", "Blade of the Heptaseas", "Hunter Strike", "Malefic Roar", "Blade of Despair", "Immortality"],
    "Ling": ["Tough Boots", "Windtalker", "Berserker's Fury", "Endless Battle", "Malefic Roar", "Immortality"],
    "Fanny": ["Tough Boots", "Bloodlust Axe", "Hunter Strike", "Malefic Roar", "Blade of Despair", "Immortality"],
    "Balmond": ["Warrior Boots", "Bloodlust Axe", "Cursed Helmet", "Dominance Ice", "Hunter Strike", "Immortality"],

    # MID LANE
    "Valir": ["Demon Shoes", "Ice Queen Wand", "Glowing Wand", "Necklace of Durance", "Athena's Shield", "Immortality"],
    "Lunox": ["Demon Shoes", "Clock of Destiny", "Lightning Truncheon", "Divine Glaive", "Holy Crystal", "Blood Wings"],
    "Eudora": ["Magic Shoes", "Clock of Destiny", "Lightning Truncheon", "Genius Wand", "Divine Glaive", "Holy Crystal"],
    "Kagura": ["Arcane Boots", "Clock of Destiny", "Lightning Truncheon", "Genius Wand", "Divine Glaive", "Holy Crystal"],
    "Luo Yi": ["Arcane Boots", "Enchanted Talisman", "Glowing Wand", "Ice Queen Wand", "Divine Glaive", "Blood Wings"],
    
    # GOLD LANE
    "Karrie": ["Swift Boots", "Corrosion Scythe", "Demon Hunter Sword", "Golden Staff", "Wind of Nature", "Athena's Shield"],
    "Claude": ["Demon Shoes", "Demon Hunter Sword", "Golden Staff", "Corrosion Scythe", "Wind of Nature", "Immortality"],
    "Moskov": ["Swift Boots", "Corrosion Scythe", "Demon Hunter Sword", "Golden Staff", "Windtalker", "Wind of Nature"]
}

# ==========================================
# 2. GUI & LOGIKA SISTEM
# ==========================================

class MLBBApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MLBB Draft Counter (Role-Based)")
        self.root.geometry("600x550")
        self.root.configure(bg="#1e1e2f")
        
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.create_widgets()

    def create_widgets(self):
        # Header
        tk.Label(self.root, text="MLBB Draft Pick Assistant", font=("Arial", 16, "bold"), bg="#1e1e2f", fg="white").pack(pady=10)

        # Frame Role Player
        frame_role = tk.Frame(self.root, bg="#1e1e2f")
        frame_role.pack(pady=5)
        
        tk.Label(frame_role, text="Pilih Role Anda:", font=("Arial", 11, "bold"), bg="#1e1e2f", fg="#7bed9f").grid(row=0, column=0, padx=10)
        self.cb_role = ttk.Combobox(frame_role, values=["Semua Role", "Jungle", "Roam", "Mid Lane", "Exp Lane", "Gold Lane"], state="readonly", width=15)
        self.cb_role.set("Jungle")
        self.cb_role.grid(row=0, column=1)

        # Frame Pemilihan Musuh
        frame_draft = tk.Frame(self.root, bg="#1e1e2f")
        frame_draft.pack(pady=15)
        
        tk.Label(frame_draft, text="Pilih Hero Musuh:", font=("Arial", 11), bg="#1e1e2f", fg="white").grid(row=0, column=0, columnspan=5, pady=5)
        
        self.enemy_comboboxes = []
        hero_list = ["-Pilih-"] + sorted(list(DATABASE_COUNTER.keys()))
        
        for i in range(5):
            cb = ttk.Combobox(frame_draft, values=hero_list, state="readonly", width=12)
            cb.set("-Pilih-")
            cb.grid(row=1, column=i, padx=5)
            self.enemy_comboboxes.append(cb)

        # Tombol Analisa
        btn_analyze = tk.Button(self.root, text="Cari Counter", command=self.analyze_draft, bg="#ff4757", fg="white", font=("Arial", 12, "bold"))
        btn_analyze.pack(pady=10)

        # Frame Hasil
        self.frame_result = tk.Frame(self.root, bg="#2f3542", bd=2, relief="groove")
        self.frame_result.pack(pady=10, fill="x", padx=30, ipady=15)
        
        self.lbl_counter_text = tk.Label(self.frame_result, text="Rekomendasi Hero Counter:", bg="#2f3542", fg="#7bed9f", font=("Arial", 12, "bold"))
        self.lbl_counter_text.pack(pady=(10, 0))
        
        self.lbl_counter_name = tk.Label(self.frame_result, text="-", bg="#2f3542", fg="white", font=("Arial", 16, "bold"))
        self.lbl_counter_name.pack(pady=5)

        tk.Label(self.frame_result, text="Rekomendasi Build Item:", bg="#2f3542", fg="#ff7f50", font=("Arial", 12, "bold")).pack(pady=(10, 5))
        
        self.lbl_items = tk.Label(self.frame_result, text="-", bg="#2f3542", fg="white", font=("Arial", 10), justify="center")
        self.lbl_items.pack(pady=5)

    def analyze_draft(self):
        selected_enemies = [cb.get() for cb in self.enemy_comboboxes if cb.get() != "-Pilih-"]
        selected_role = self.cb_role.get()
        
        if not selected_enemies:
            self.lbl_counter_name.config(text="Silakan pilih minimal 1 musuh!")
            self.lbl_items.config(text="-")
            return

        # 1. Kumpulkan semua hero counter mentah dari musuh yang dipilih
        raw_counters = []
        for enemy in selected_enemies:
            if enemy in DATABASE_COUNTER:
                raw_counters.extend(DATABASE_COUNTER[enemy])

        # 2. Filter counter berdasarkan Role yang dimainkan user
        valid_counters = []
        for counter in raw_counters:
            # Periksa apakah hero tersebut memiliki role yang sesuai (atau jika user memilih "Semua Role")
            roles_for_hero = HERO_ROLES.get(counter, [])
            if selected_role == "Semua Role" or selected_role in roles_for_hero:
                valid_counters.append(counter)

        # 3. Cari yang terbanyak muncul (irisan terbaik)
        if not valid_counters:
            self.lbl_counter_name.config(text=f"Tidak ada counter {selected_role} untuk kombinasi ini.")
            self.lbl_items.config(text="-")
            return

        counter_tally = Counter(valid_counters)
        best_counter = counter_tally.most_common(1)[0][0]

        # Menampilkan Hasil Hero
        self.lbl_counter_name.config(text=f"⭐ {best_counter} ⭐")
        
        # Menampilkan Hasil Build Item (Teks Saja)
        build = DATABASE_BUILD.get(best_counter, ["Gunakan Build Pro/Default di dalam game"])
        
        # Format item menjadi string rapi (baris baru setiap 3 item)
        item_text = ""
        for idx, item in enumerate(build):
            item_text += f"• {item}   "
            if (idx + 1) % 3 == 0:
                item_text += "\n"
                
        self.lbl_items.config(text=item_text.strip())

# ==========================================
# 3. JALANKAN APLIKASI
# ==========================================
if __name__ == "__main__":
    root = tk.Tk()
    app = MLBBApp(root)
    root.mainloop()
