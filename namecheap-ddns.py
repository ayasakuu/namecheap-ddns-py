import requests
from sys import argv

# py -3 namecheap-ddns.py HOST DOMAIN_NAME PASSWORD

ipr = requests.get("https://dynamicdns.park-your-domain.com/getip")
if ipr.status_code == 200:
    requests.get(f"https://dynamicdns.park-your-domain.com/update?host={argv[1]}&domain={argv[2]}&password={argv[3]}&ip={ipr.content.decode('utf-8')}")