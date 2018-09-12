import requests

TOKEN = "624490139:AAFfbzXhtAKhbUGMz_wXTTo3ZFHxpqglQp0"
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'
r = requests.get(f"{MAIN_URL}/getMe")

r = requests.get("https://api.telegram.org/bot624490139:AAFfbzXhtAKhbUGMz_wXTTo3ZFHxpqglQp0/getMe")
print(r.json())



