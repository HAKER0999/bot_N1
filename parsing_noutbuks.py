import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
noutbuklar = []
host_url ="https://ultrashop.uz/ru/store/noutbuki"
url = "https://ultrashop.uz/ru/store/noutbuki"
response = requests.get(url, headers=headers)

html = response.text
soup = BeautifulSoup(html, 'html.parser')
main = soup.find("div", class_="row px-3")
# print(main)
main_block = main.find_all("div", class_="list-complete-item w-100")
# print(main_block)
for product in main_block:
    product_name = product.find("h1", class_="h6").get_text()
    # print(product_name)
    product_price = product.find("div", class_="list-view__price").get_text()
    # print(product_price)
    product_image = product.find("div", class_="list-view__img mr-4").find("img")["src"]
    # print(product_image)

    noutbuklar.append({
        "Product_name": product_name,
        "Product_price": product_price,
        "Product_image": product_image
    })
# print(noutbuks)