import requests
link="https://www.w3schools.com/python/default.asp"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
r=requests.get(link,headers=headers)

# print(r.text)
print(r.status_code)   # 200 = success, 404 = not found, etc.
print(r.headers)       # response headers (content type, server info, etc.)
print(len(r.text))     # how much text was returned
print(r.text[:500])  # first 500 characters only
