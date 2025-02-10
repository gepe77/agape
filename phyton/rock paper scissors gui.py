import tkinter as tk
import random

gameitem = [" rock", " paper" ," scissors"] #ini adalah list. list adalah command yang digunakan untuk mumat banyak item dalam 1 variable
#valitadi stands for (variable list tuple dictionary) tingkatan cupu to suhu

pilkom = random.choice(gameitem)

def pilwin(pilkom,pilplay):
    if pilplay == pilkom:
        return "its a tie"
    elif pilplay == "scissors" and pilkom == "paper":#agape cari tahu pake operator logika yang mana miggu depan sudah ketemu jawabanya dan alasanya
        return " player win"
    elif pilplay == "rock" and pilkom == "scissors":
        return " player win"
    elif pilplay == "paper" and pilkom == "rock":
        return " player win"
    else:
        return" player lose😣"

def buttonkonek(player):
    komputer = random.choice(gameitem)
    hasil = pilwin(komputer,player) #pilwin dipanggil pilwin punya 2 slot yaitu pilkom dan pilplay, maka saat di panggil lagi pilwin harus punya 2 parameter
    whatchoose.config(text=f"komputer milih:{komputer}")
    whowin.config(text=f"hasilnya adalah:{hasil}")

jendela = tk.Tk() #jendela adalah seluruh bagian dari aplikasi yang memuat label dan tombol 
jendela.title("lps game by agape tampan")

intro = tk.Label(jendela,text = "tekan salah satu tombol: rock,paper,atau scissors")
intro.pack(pady = 5)

buttonr = tk.Button(jendela,text = "rock",command=lambda:buttonkonek("rock"))
buttonr.pack(pady = 10)

buttonp = tk.Button(jendela,text = "paper",command=lambda:buttonkonek("paper"))
buttonp.pack(pady = 10)

buttons = tk.Button(jendela,text = "scissors",command=lambda:buttonkonek("scissors"))
buttons.pack(pady = 10)

whowin = tk.Label(jendela,text = "")
whowin.pack(pady = 10)

whatchoose = tk.Label(jendela,text = "")
whatchoose.pack(pady = 10)

credits = tk.Label(jendela,text = "by agape")
credits.pack(pady = 10)

jendela.mainloop() #main loop adalah perintah terakhir dari semua script atau perintah dari tkinter