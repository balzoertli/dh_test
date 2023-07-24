import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter, Retry

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

url = "https://www.efk.admin.ch/de/politikfinanzierung/aufgaben-der-efk/kontrollen.html"
response = session.get(url)

soup = BeautifulSoup(page.content, "lxml")
elements = soup.find(id="collapse4")
print(elements.text.strip())

