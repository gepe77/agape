import tkinter as tk
import threading
import random
import time

# Fungsi untuk membuat pop-up yang bergerak
def create_popup():
    window = tk.Tk()
    window.title("JAWA = HAMA")
    window.geometry("300x150+100+100")

    label = tk.Label(window, text="JAWA = HAMA", font=("Arial", 14, "bold"), fg="black")
    label.pack(expand=True)

    # Fungsi untuk menggerakkan jendela
    def move_window():
        if window.winfo_exists():  # Cek apakah jendela masih ada
            x = random.randint(0, window.winfo_screenwidth() - 300)
            y = random.randint(0, window.winfo_screenheight() - 150)
            window.geometry(f"300x150+{x}+{y}")
            window.after(200, move_window)  # Pindah setiap 0.2 detik

    move_window()
    window.mainloop()

# Buka pop-up bertahap biar gak nge-lag
for i in range(20):  # Bisa diubah jumlahnya
    threading.Thread(target=create_popup, daemon=True).start()
    time.sleep(1.5)  # Delay biar gak langsung muncul semua
