import requests

API_KEY = "rxM8D6n6RrdmmJA5uW2KQg==pJcpzaY9CtCVGhDg"
API_URL = "https://api.api-ninjas.com/v1/animals?name={}"


def fetch_data(animal_name):
    url = API_URL.format(animal_name)
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(url, headers = headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}, {response.text}")