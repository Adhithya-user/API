import requests

response=requests.get(url="http://api.open-notify.org/iss-now.json")

print(response)
print(response.json())


"""import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.status_code)
print(response.json())"""
