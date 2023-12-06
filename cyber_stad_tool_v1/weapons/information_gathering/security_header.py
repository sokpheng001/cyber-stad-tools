import time
import requests
from tqdm import tqdm
from components import loading

def security_header_scan(url):
    print("\033[34m[+] Scanning in progress:\033[0m")  # \033[34m sets the text color to blue
    # for _ in tqdm(range(10), desc="\033[34m[+] Waiting\033[0m", colour='blue'):  # \033[31m sets the text color to red
    #     time.sleep(0.5)
    loading.loading_animation()
    print("\033[34m[+] Scanning...\033[0m")
    # Ensure the URL has a default protocol (https if none provided)
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url

    try:
        # Attempt to make the HTTP request
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Accessing HTTP headers
            headers = response.headers

            # Print all headers
            print("HTTP Headers:")
            for key, value in headers.items():
                print(f"[+] {key}: {value}")

        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        # Handle any exception that might occur during the request
        print(f"Error during the HTTP request: {e}")

