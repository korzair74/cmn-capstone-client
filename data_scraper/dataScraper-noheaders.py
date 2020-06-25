import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://ark.gamepedia.com/Rex")
bsObj = BeautifulSoup(html, 'lxml')
table = bsObj.findAll("table", {"class": "wikitable"})[19]
rows = table.findAll('tr')
csvFile = open("./rex150.csv", 'wt', newline='')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
