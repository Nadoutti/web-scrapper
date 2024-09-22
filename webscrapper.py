import requests
from bs4 import BeautifulSoup

url = input("Cole a url de algum site: ")

response = requests.get(url)

if response.status_code == 200:
    processed = response.content

    soup = BeautifulSoup(processed, 'html.parser')
    print(soup.title.string)
else:
    print("Houve um problema com o programa")
