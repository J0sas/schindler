import requests
from bs4 import BeautifulSoup

url = "https://www.linkedin.com/in/caiojosue/overlay/contact-info/"
r = requests.session()
html = r.get(url)
soup = BeautifulSoup(html.text, "html.parser")
print(soup)
