import requests
from bs4 import BeautifulSoup
import re
import json
API_KEY = "CTtOMH2zx2XyOVipNl6qmdSLPJV7oRWq"
API_KEY2 = "f8e6fd8e886541e783d160dc60faf44e"

header_content = {'Content-Type': 'text/raw',
'x-ag-access-token': API_KEY,
'outputFormat': 'application/json'}

def tag_content(content_string):
    tags_list = []
    content_string = content_string.encode('utf-8')
    response = requests.post('https://api-eit.refinitiv.com/permid/calais', headers=header_content, data=content_string)
    jsonResponse = response.json()
    for obj in jsonResponse:
         try:
             tags_list += [jsonResponse[obj]['name']]
         except:
             tags_list += []
    return tags_list


class scraper:
    def __init__(self, URL):
        self.URL = URL
        self.page = requests.get(URL)
        self.soup = BeautifulSoup(self.page.content,'html.parser')
        self.title = self.soup.find('head').find('title').text
        self.imgscr = "https://revenuearchitects.com/wp-content/uploads/2017/02/Blog_pic-450x255.png"
        try:   
            self.imgsrc = self.soup.find('img')['src']
        except:
            self.imgsrc = "https://revenuearchitects.com/wp-content/uploads/2017/02/Blog_pic-450x255.png"
        self.description = ""
        for meta in self.soup.find('head').find_all('meta'):
            try:
                if meta['name'] == 'description':
                    self.description = meta['content']
            except:
                self.description = ""
        for para in self.soup.find_all('p'):
            if(len(self.description)>500):
                break
            self.description += para.text
        self.description = re.sub(' +', ' ', self.description)
        self.description = self.description.replace("\n", "")
        self.tags = tag_content(self.description)
        
    def __str__(self):
        return "Title: " + self.title + "\nDescription: " + self.description + "\nimage: " + self.imgsrc


class discoverScraper:
    def __init__(self, article):
        self.URL = article['url']
        try:   
            self.imgsrc = article['urltoimage']
        except:
            self.imgsrc = "https://revenuearchitects.com/wp-content/uploads/2017/02/Blog_pic-450x255.png"
        self.title = article['title']
        self.description = article['description']
        self.tags = tag_content(self.description)
    def __str__(self):
        return "Title: " + self.title + "\nDescription: " + self.description + "\nimage: " + self.imgsrc
