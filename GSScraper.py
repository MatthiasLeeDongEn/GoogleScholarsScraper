from bs4 import BeautifulSoup
import requests
import csv

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

#Input desired URL from Google Scholars
print('Please paste URL of desired Google Scholars page')
url = str(input())
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content,'lxml')

#Input desired file name
filename = 'Google_Scholar_Table' + '.csv'

csv_file = open(filename, 'w', newline = "")
csv_writer = csv.writer(csv_file, delimiter = ',')
csv_writer.writerow(['Title','Author','Summary','Link'])

#Creation of data in the table format
for item in soup.select('[data-lid]'):
    try:
        title = item.select('h3')[0].get_text()
        author = item.select('.gs_a')[0].get_text()
        link = item.select('a')[0]['href']
        # Use this if format does not detect hyperlink automatically
        fullLink = str("=HYPERLINK(" + "\"" + (link) +  "\"" + ")") 
        summary = item.select('.gs_rs')[0].get_text()
        csv_writer.writerow([title, author, summary, fullLink])
        
    except Exception as e:
        print('')


csv_file.close
