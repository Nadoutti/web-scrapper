import requests
from bs4 import BeautifulSoup

url = "https://www.bawclothing.com.br/baw/vestuario/partes-de-cima/camisetas?page=3"

response = requests.get(url)

if response.status_code == 200:
    processed = response.content

    soup = BeautifulSoup(processed, 'html.parser')
    title = soup.title.text
    spans = soup.find_all('span')
    precos = []
    receita = 0
    for span in spans:
        if 'x' not in span.text:
            if 'R$' in span.text:
                precos.append(span.string.strip("R$\xa0"))
    
    for preco in precos:
        receita += int(preco.strip(',00'))
    print(f"A empresa {title} faria R$ {receita} se vendesse cada um dos produtos em um mes.")

else:
    print("Houve um problema com o programa")
