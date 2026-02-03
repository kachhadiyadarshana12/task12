import requests 
import json

url = "https://randomuser.me/api/"

try:
    response = requests.get(url, timeout=10) # get request
    response.raise_for_status() # error raise
    data = response.json() # python dictionary in convert
    user = data["results"][0] # required fields extract

    first_name = user["name"]["first"]
    last_name = user["name"]["last"]
    email = user["email"]
    username = user["login"]["username"]
    country = user["location"]["country"]

    print("--User Details--")
    print("----------------")
    print("Name     : ", first_name, last_name)
    print("Email    : ", email)
    print("Username : ", username)
    print("Country  : ", country)

    with open("api_response.json", "w", encoding="utf-8") as file:  # json fine in save
        json.dump(data, file, indent=4)
    
    print("\n API data successfully saved in api_response.json")

except requests.exceptions.RequestException as error: # api error handle
    print("Error while fetching API data : ", error)