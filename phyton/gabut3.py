import time
import sys

# Lirik lagu dengan waktu kemunculan (detik, lirik)
lirik_lagu = [
    (0, "🎵 When I was a young boy, 🎵"),
    (4, "🎵 My father took me into the city 🎵"),
    (9, "🎵 To see a marching band. 🎵"),
    (14, "🎵 He said, 'Son, when you grow up, 🎵"),
    (19, "🎵 Would you be the savior of the broken, 🎵"),
    (24, "🎵 The beaten and the damned?' 🎵"),
    (30, "🎵 He said, 'Will you defeat them? 🎵"),
    (34, "🎵 Your demons and all the non-believers, 🎵"),
    (39, "🎵 The plans that they have made?' 🎵"),
    (44, "🎵 Because one day, I'll leave you 🎵"),
    (49, "🎵 A phantom to lead you in the summer 🎵"),
    (54, "🎵 To join the black parade.' 🎵"),
]

def type_text(teks, delay=0.05):
    """Menampilkan teks dengan efek mengetik huruf per huruf."""
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(delay)  # Delay antar huruf
    print()  # Pindah ke baris baru setelah teks selesai

# Waktu mulai
start_time = time.time()

# Menampilkan lirik sesuai waktu
for detik, teks in lirik_lagu:
    while time.time() - start_time < detik:
        time.sleep(0.1)  # Tunggu sampai waktunya tiba
    type_text(teks, delay=0.05)  # Efek mengetik
