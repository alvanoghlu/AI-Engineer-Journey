
import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=10)
    print("Status code:", response.status_code)

    response.raise_for_status()

    print("Request successful!")

except requests.exceptions.RequestException as error:
    print("An error occurred:", error)


response = requests.get(url)

print("Status Code:",response.status_code)

users = response.json()

print("Total users:", len(users))
print(users[0])


for user in users:
    name = user["name"]
    email = user["email"]
    city = user["address"]["city"]

    print("Name:", name)
    print("Email:", email)
    print("City:", city)
    print("--------------------")