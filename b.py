# Auto Import Installer
import os
try:
    import threading, time, os, colorama, pyfiglet, random
    from threading import Thread, Lock
    from colorama import Fore, Style, Back
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    print(f"\n{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] {Fore.RESET}Imports successful!")
    time.sleep(1)
except:
    print("\nImports failed! Trying to install...")
    z = "python -m pip install "; os.system('%srequests' % (z)); os.system('%scolorama' % (z)); os.system('%sthreading' % (z)); os.system('%sos-sys' % (z)); os.system('%sthreading' % (z)); os.system('%srandom' % (z)); os.system('%spyfiglet' % (z))
    print(f"\n{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] {Fore.RESET}Imports successful!")
    time.sleep(1)

# Imports
import threading, time, os, colorama, pyfiglet, random
from threading import Thread, Lock
from colorama import Fore, Style, Back
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Variables
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
os.system(f"title GitHub View Booster - Ready! - discord.gg/kws")
logo = pyfiglet.figlet_format("GitHub Viewer", font="smkeyboard")
clear()

# Lock prints to threads to avoid skipping new lines
lock = Lock()
def doprint(msg):
    with lock:
        print(msg)

# Ask user for input
count = 0
proxyDebug = False # Set to True to see proxy debug messages
print(logo + Fore.MAGENTA +"\nhttps://github.com/kWAYTV\n\n" + Fore.RESET)
profile = input(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} Enter the username you want to send the views to (just the {Fore.MAGENTA}exact{Fore.RESET} name): @")
views = input(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} Enter the amount of views you want to send to the profile (number will increase a bit depending on threads): ")
threads = input(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} Enter the amount of threads you want to use: ")
proxylessChoice = input(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} Do you want to use proxies? (y/n): ")
if proxylessChoice == "y":
    proxyless = False
    debug = input(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} Do you want to see proxy debug messages? (y/n): ")
    if debug == "y":
        proxyDebug = True
    elif debug == "n":
        proxyDebug = False
    else:
        print(f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Invalid option.")
        time.sleep(3)
        exit()
elif proxylessChoice == "n":
    proxyless = True
else:
    print(f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Invalid option.")
    time.sleep(3)
    exit()

# Main function
os.system(f"title GitHub View Booster - Working... - discord.gg/kws")
def boost(lock):
    global count
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.3610")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    if proxyless == False:
        with open("proxies.txt", "r") as f:
            proxies = f.read().splitlines()
            proxy = random.choice(proxies)
            f.close()
        chrome_options.add_argument(f"--proxy-server={proxy}")
    else:
        pass
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(f"https://github.com/{profile}")
    time.sleep(3)
    count += 1
    if proxyDebug == True:
        doprint(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} @{Fore.MAGENTA}{profile}{Fore.RESET}'s Github Visited: {Fore.GREEN}{count}{Fore.RESET} times. Proxy: {Fore.MAGENTA}{proxy}{Fore.RESET}")
    else:
        doprint(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} @{Fore.MAGENTA}{profile}{Fore.RESET}'s Github Visited: {Fore.GREEN}{count}{Fore.RESET} times.")
    driver.quit()
    os.system(f"title GitHub View Booster - Views: {count}/{views} - Threads: {threads} - Profile: @{profile}")

# Start and threading
def start():
    tArray = []
    try:
        clear()
        print(logo + Fore.MAGENTA +"\nhttps://github.com/kWAYTV\n\n" + Fore.RESET)
        print(f"{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}]{Fore.RESET} Started sending {Fore.MAGENTA}{int(views)}{Fore.RESET} views to @{Fore.MAGENTA}{profile}{Fore.RESET} with {Fore.MAGENTA}{int(threads)}{Fore.RESET} threads.\n")
        start = time.time()
        # Make the threads run until all views are done with safe printing  
        while count <= (int(views) - int(threads)):
            for i in range(int(threads)):
                t = Thread(target=boost, args=(lock,))
                tArray.append(t)
                t.start()
            for t in tArray:
                t.join()
        print(f"{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}]{Fore.RESET} All threads stopped.")
        end = time.time() 
        doprint(f"\n{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}]{Fore.RESET} Finished sending {Fore.MAGENTA}{int(views)}{Fore.RESET} views to @{Fore.MAGENTA}{profile}{Fore.RESET} with {Fore.MAGENTA}{int(threads)}{Fore.RESET} threads in {Fore.MAGENTA}{round(end-start,2)}{Fore.RESET} seconds.")
        os.system(f"title GitHub View Booster - Finished! - Elapsed {round(end-start,2)} seconds - discord.gg/kws")
        input(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} Press any key to exit.")
        time.sleep(1)
        os._exit(1)
    except KeyboardInterrupt():
        print(f"\n{Fore.RED}[{Fore.RESET}X{Fore.RED}]{Fore.RESET} User stopped the script.")
        os.system(f"title GitHub View Booster - Stopped! - discord.gg/kws")
        input(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} Press any key to exit.")
        time.sleep(1)
        os._exit(1)
    except Exception as e:
        print(f"\n{Fore.RED}[{Fore.RESET}X{Fore.RED}]{Fore.RESET} Error: {str(e)}")
        os.system(f"title GitHub View Booster - Error! - discord.gg/kws")
        input(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} Press any key to exit.")
        time.sleep(1)
        os._exit(1)

start()