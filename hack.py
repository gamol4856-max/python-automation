import time
import os

from colorama import Fore, Style, init

init()

# clear screen
os.system("cls" if os.name == "nt" else "clear")

lines = [
    "[+] Initializing system core...",
    "[+] Loading encrypted modules...",
    "[+] Bypassing security layers...",
    "[+] Establishing secure tunnel...",
    "[+] Decrypting payload...",
    "[+] ACCESS GRANTED ✔"
]

def type_line(text, delay=0.04):
    for ch in text:
        print(Fore.GREEN + ch, end="", flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

for line in lines:
    type_line(line)
    time.sleep(0.7)

input(Fore.GREEN + "\nPress ENTER to exit...")