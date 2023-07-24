import requests
from bs4 import BeautifulSoup

url = "https://www.efk.admin.ch/de/politikfinanzierung/aufgaben-der-efk/kontrollen.html"
entries = []
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")
elements = soup.find(id="collapse4")
print(elements.text.strip())
