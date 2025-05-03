import winsound
import time


NOTES = {
    'A': 262, 'B': 294, 'C': 330, 'D': 349, 'E': 392,
    'F': 440, 'G': 494, 'H': 523, 'I': 587, 'J': 659,
    'K': 698, 'L': 784, 'M': 880, 'N': 988, 'O': 1047,
    'P': 1175, 'Q': 1319, 'R': 1397, 'S': 1568, 'T': 1760,
    'U': 1976, 'V': 2093, 'W': 2349, 'X': 2637, 'Y': 2794,
    'Z': 3136, ' ': 0  
}

DURATION = 300  
def play_secret_tone(text):
    for char in text.upper():
        if char in NOTES:
            freq = NOTES[char]
            if freq > 0:
                winsound.Beep(freq, DURATION)
            time.sleep(0.1)  

    print("\n Kode rahasia selesai!")


text = input("Masukkan teks rahasia: ")
play_secret_tone(text)
