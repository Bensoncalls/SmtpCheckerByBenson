import smtplib
from colorama import Fore

ascii_logo = """

 ____            _                _____  __    ___  ____
/ ___| _ __ ___ | |_ _ __   __  _|___ / / /_  / _ \| __ ) _   _
\___ \| '_ ` _ \| __| '_ \  \ \/ / |_ \| '_ \| | | |  _ \| | | |
 ___) | | | | | | |_| |_) |  >  < ___) | (_) | |_| | |_) | |_| |
|____/|_| |_| |_|\__| .__/  /_/\_\____/ \___/ \___/|____/ \__, |
                    |_|                                   |___/
 ____
| __ )  ___ _ __  ___  ___  _ __
|  _ \ / _ \ '_ \/ __|/ _ \| '_ \
| |_) |  __/ | | \__ \ (_) | | | |
|____/ \___|_| |_|___/\___/|_| |_|
"""
print(ascii_logo)


Fore.RESET
Fore.GREEN
Fore.RED

def check_smtp_capabilities(host, port, username, password):
    try:
        smtp = smtplib.SMTP(host, port, timeout=10)  # Set a timeout of 10 seconds
        smtp.starttls()
        smtp.login(username, password)
        
        print(f"{Fore.GREEN}SMTP server {host}:{port} authentication successful for {username}")

        
        max_rcpt_limit = smtp.esmtp_features.get('size', 0)
        print(f"Max recipients allowed: {max_rcpt_limit}")

        
        smtp.quit()
    except Exception as e:
        print(f"{Fore.RED}SMTP server {host}:{port} authentication failed: {e}")

def read_smtp_servers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            smtp_servers = [line.strip().split('|') for line in file.readlines()]
            return smtp_servers
    except FileNotFoundError:
        print("File not found")
        return []

file_path = input("Enter path to the file containing SMTP server details: ")

smtp_servers = read_smtp_servers_from_file(file_path)
if smtp_servers:
    for server in smtp_servers:
        if len(server) == 4:
            check_smtp_capabilities(*server)

