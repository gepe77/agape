import tkinter as tk
import math
from tkinter import messagebox

# Fungsi untuk menembak
def shoot():
    try:
        angle = float(angle_entry.get())
        velocity = float(velocity_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")
        return
    
    rad_angle = math.radians(angle)
    v_x = velocity * math.cos(rad_angle)
    v_y = -velocity * math.sin(rad_angle)
    G = 9.8
    
    proj_x, proj_y = 100, 350
    t = 0
    
    # Hapus tembakan sebelumnya
    canvas.delete("projectile")
    
    while proj_x < 600 and proj_y < 400:
        proj_x = 100 + v_x * t
        proj_y = 350 + v_y * t + 0.5 * G * t ** 2
        t += 0.1
        canvas.create_oval(proj_x, proj_y, proj_x + 5, proj_y + 5, fill="red", tags="projectile")
        canvas.update()
        canvas.after(10)
        
        if 500 <= proj_x <= 540 and proj_y >= 360:
            messagebox.showinfo("Menang!", "Bunker berhasil dihancurkan!")
            return
    
    messagebox.showinfo("Gagal", "Tembakan meleset! Coba lagi.")

# GUI Tkinter
root = tk.Tk()
root.title("Komandan Artileri")

story_label = tk.Label(root, text="Anda adalah Komandan Artileri! Musuh bersembunyi di bunker, dan tugas Anda adalah menghancurkannya dengan tembakan yang tepat!", wraplength=400, justify="left")
story_label.pack(pady=10)

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()
canvas.create_rectangle(500, 360, 540, 400, fill="green")
canvas.create_oval(90, 340, 110, 360, fill="black")

controls_frame = tk.Frame(root)
controls_frame.pack(pady=10)

tk.Label(controls_frame, text="Sudut (°):").grid(row=0, column=0)
angle_entry = tk.Entry(controls_frame)
angle_entry.grid(row=0, column=1)
angle_entry.insert(0, "45")

tk.Label(controls_frame, text="Kecepatan (m/s):").grid(row=1, column=0)
velocity_entry = tk.Entry(controls_frame)
velocity_entry.grid(row=1, column=1)
velocity_entry.insert(0, "50")

tk.Button(root, text="Tembak!", command=shoot).pack()

root.mainloop()