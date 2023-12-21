import nmap
from tqdm import tqdm
import time
from components import loading

def perform_port_scan(target_host):
    print("\033[34m[+] Scanning in progress:\033[0m")  # \033[34m sets the text color to blue
    # for _ in tqdm(range(10), desc="\033[34m[+] Waiting\033[0m", colour='blue'):  # \033[31m sets the text color to red
    #     time.sleep(0.5)
    loading.loading_animation()
    print("\033[34m[+] Scanning...\033[0m")
    target_ports = "1-10000"  # You can adjust the port range as needed
    nm = nmap.PortScanner()
    nm.scan(target_host, target_ports)

    for host in nm.all_hosts():
        print(f"[+] Results for {host}")
        print("-" * 40)
        for proto in nm[host].all_protocols():
            print(f"[+] Protocol: {proto}")
            print("-" * 20)
            ports = nm[host][proto].keys()
            for port in ports:
                port_info = nm[host][proto][port]
                print(f"[+] Port: {port}\tState: {port_info['state']}\tService: {port_info['name']}")

                # Check if service version information is available
                if 'product' in port_info and 'version' in port_info:
                    print(f"  server: {port_info['product']} {port_info['version']}")
                elif 'product' in port_info:
                    print(f"  server: {port_info['product']}")

# if __name__ == "__main__":
#     target_host = "istad.co"  # Replace with the target website
#     perform_port_scan(target_host)
