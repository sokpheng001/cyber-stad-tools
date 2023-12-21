import time
import sys
import psutil
from colorama import Fore, init, Style

# Initialize colorama
init(autoreset=True)

def get_cpu_usage():
    return psutil.cpu_percent(interval=0.01)

def loading_animation(content=None):
    if content is None:
        content = "Starting tool"
    else:
        content=content;
    opening_text = "Opening"
    loading_text = "Loading"
    width = 40  # Width of the progress bar
    for i in range(width + 1):
        progress = i / width
        block = "█" * int(width * progress)
        spaces = " " * (width - int(width * progress))
        sys.stdout.write("\r" + Fore.RED + f"[+] {content}: [" + block + spaces + "] {:.0%}".format(progress))
        sys.stdout.flush()

        # Adjust sleep duration based on CPU usage
        sleep_duration = 0.1 / (get_cpu_usage() / 100 + 1)
        time.sleep(sleep_duration)

    # sys.stdout.write("\r" + Fore.GREEN + "[+] Started tool: [" + "█" * width + "] 100%  \n")
    sys.stdout.write("\r" + " " * (len(opening_text) + 3 + width + 20) + "\n")
    print("[" + Fore.GREEN + "*" + Style.RESET_ALL +"] "+ "Tool Started!");
    print("...................................\n");

