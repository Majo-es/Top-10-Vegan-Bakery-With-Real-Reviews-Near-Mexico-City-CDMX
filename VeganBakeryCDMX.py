import requests #allows you to send HTTP requests using Python
from bs4 import BeautifulSoup

url = "https://www.yelp.com/search?find_desc=Vegan+Bakery&find_loc=Mexico+City%2C+CDMX%2C+Mexico"

#Use requests to get the webpage as text. When printing the html, we get back just how much info there is contained in the page.
response = requests.get(url)
html = response.text

#Use BeautifulSoup to parse the html. BeautifulSoup is a library that will help us parse the html
soup = BeautifulSoup(html, 'html.parser')

myLinks = soup.find_all("a", {"class":"y-css-12ly5yx"})
print(len(myLinks))

#ADD A COUNTER:
counter = 0
# LOOP THROUGH THE LINKS:
for link in myLinks:
  print(link.text)
  
print(f"""https://www.yelp.com{link["href"]}""") # fString to add the relative address
counter +=1
  
