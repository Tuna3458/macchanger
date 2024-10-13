import random
import subprocess
import time
while True:
    x = random.randint(0, 1000)

    dosya = open("/home/tuna/Downloads/bfotool-download(2).txt", "r")
    liste = dosya.readlines()
    y = (liste[x])
    subprocess.call(["ifconfig", "eth0", "down"])
    subprocess.call(["ifconfig", "eth0", "hw", "ether", y])
    subprocess.call(["ifconfig", "eth0", "up"])
    time.sleep(3)




