import socket
import threading
import requests
from queue import Queue
from colorama import init, Fore

init(autoreset=True)

print(Fore.CYAN + "\n[+] Starting Port Scanner...\n")

target = input("Enter Target IP or Domain: ")
print(f"Scanning {target} for open ports...\n")

# Range of ports to scan
start_port = 1
end_port = 1024  # You can increase later

# Thread-safe queue to hold ports
port_queue = Queue()

open_ports = []

# Worker function to scan ports
def port_scan():
    while not port_queue.empty():
        port = port_queue.get()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            result = sock.connect_ex((target, port))
            if result == 0:
                print(Fore.GREEN + f"[+] Port {port} is OPEN")
                open_ports.append(port)
            sock.close()
        except Exception as e:
            pass
        port_queue.task_done()

# Fill the queue with ports
for port in range(start_port, end_port + 1):
    port_queue.put(port)

# Create and start threads
thread_count = 100  # Number of threads
threads = []

for _ in range(thread_count):
    t = threading.Thread(target=port_scan)
    t.daemon = True
    t.start()
    threads.append(t)

# Wait for all threads to finish
port_queue.join()

print(Fore.CYAN + "\n[+] Scan Complete!")
print(Fore.YELLOW + f"Open ports: {open_ports}")



def analyze_headers(target_url):
    print(Fore.CYAN + f"\n[+] Analyzing HTTP headers for {target_url}...\n")
    try:
        response = requests.get(target_url)
        headers = response.headers

        important_headers = [
            "Content-Security-Policy",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "Strict-Transport-Security",
            "Referrer-Policy",
            "Permissions-Policy",
        ]

        for header in important_headers:
            if header in headers:
                print(Fore.GREEN + f"[+] {header} is present")
            else:
                print(Fore.RED + f"[-] {header} is MISSING")

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[-] Error fetching headers: {e}")

# Ask user if they want to analyze headers
choice = input("\nDo you want to analyze HTTP headers of a website? (yes/no): ").strip().lower()

if choice == "yes":
    website = input("Enter the website URL (include http:// or https://): ").strip()
    analyze_headers(website)
else:
    print(Fore.YELLOW + "Skipping HTTP header analysis.")

def directory_bruteforce(base_url, wordlist_file):
    print(Fore.CYAN + f"\n[+] Starting Directory Brute-Force on {base_url}\n")

    try:
        with open(wordlist_file, 'r') as f:
            directories = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(Fore.RED + f"[-] Wordlist file '{wordlist_file}' not found!")
        return

    found_dirs = []

    for directory in directories:
        url = base_url.rstrip('/') + '/' + directory
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Found: {url} (Status: {response.status_code})")
                found_dirs.append(url)
            else:
                print(Fore.YELLOW + f"[-] Not found: {url} (Status: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"[-] Error requesting {url}: {e}")

    print(Fore.CYAN + "\n[+] Directory Brute-Force Complete!")
    if found_dirs:
        print(Fore.YELLOW + f"Found directories:\n" + "\n".join(found_dirs))
    else:
        print(Fore.YELLOW + "No directories found.")

# Ask user if they want to run the directory brute-force scanner
choice = input("\nDo you want to run directory brute-force on a website? (yes/no): ").strip().lower()

if choice == "yes":
    website = input("Enter the website URL (include http:// or https://): ").strip()
    wordlist_path = "common_directories.txt"  # make sure this file exists in the same folder
    directory_bruteforce(website, wordlist_path)
else:
    print(Fore.YELLOW + "Skipping directory brute-force.")
