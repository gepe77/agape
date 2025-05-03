import tkinter as tk
from tkinter import messagebox

# Inisialisasi GUI
root = tk.Tk()
root.title("HOI4 Python Clone")
root.geometry("800x600")

# Peta Dunia (Placeholder)
canvas = tk.Canvas(root, width=800, height=400, bg="lightblue")
canvas.pack()

# Negara-negara (Placeholder)
nations = {
    "Germany": {"troops": 100, "factories": 50, "resources": 80},
    "USA": {"troops": 150, "factories": 70, "resources": 100},
    "USSR": {"troops": 200, "factories": 60, "resources": 90}
}

# Menampilkan informasi negara
info_label = tk.Label(root, text="Pilih negara untuk melihat detail", font=("Arial", 14))
info_label.pack()

def show_nation_info(nation):
    """Menampilkan informasi negara yang dipilih"""
    data = nations[nation]
    info_label.config(text=f"{nation}\nTroops: {data['troops']}\nFactories: {data['factories']}\nResources: {data['resources']}")

def attack(target):
    """Menyerang negara lain"""
    if target in nations:
        nations[target]["troops"] -= 20
        if nations[target]["troops"] <= 0:
            messagebox.showinfo("Victory!", f"{target} has been conquered!")
            del nations[target]
        show_nation_info(target)

# Tombol negara
germany_btn = tk.Button(root, text="Germany", command=lambda: show_nation_info("Germany"))
germany_btn.pack()
usa_btn = tk.Button(root, text="USA", command=lambda: show_nation_info("USA"))
usa_btn.pack()
ussr_btn = tk.Button(root, text="USSR", command=lambda: show_nation_info("USSR"))
ussr_btn.pack()

# Tombol serangan
attack_btn = tk.Button(root, text="Attack USSR", command=lambda: attack("USSR"))
attack_btn.pack()

root.mainloop()
