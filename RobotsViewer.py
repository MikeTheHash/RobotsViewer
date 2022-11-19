import requests
import argparse
import colorama
import platform
import time
import os
import banner

system = platform.system()

banner.banner()

print(colorama.Back.RED + colorama.Fore.WHITE + "[+] You can see the parameters using \"-h\" or \"--help\"")
print(colorama.Back.RED + colorama.Fore.WHITE + "[+] You must set the parameters!" + colorama.Style.RESET_ALL )
time.sleep(1.5)
if system == "windows":
    os.system("cls")
else:
    os.system("clear")
banner.banner()
parser = argparse.ArgumentParser()
parser.add_argument("--target", help="set your target")
args = parser.parse_args()
args.target = str(args.target) + "/robots.txt"

try:
    r = requests.get(f"{args.target}")
    if r.status_code == 404 or r.status_code == str(404):
        print("[-] Robots.txt file not found")
    else:
        print("")
        print("[+] Robots.txt file found")
        print(f"[+] Robots.txt content:")
        print(r.text).replace("\\\n")
except:
    pass
