import requests

url = "https://api.github.com"

response = requests.get(url)

print("Status Code:", response.status_code)
print()
print(response.text)