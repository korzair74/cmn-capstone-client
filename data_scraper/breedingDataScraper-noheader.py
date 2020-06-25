import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://ark.gamepedia.com/Table_of_Breeding")
bsObj = BeautifulSoup(html, 'lxml')
table = bsObj.findAll("table", {"class": "wikitable"})[0]
rows = table.findAll('tr')
csvFile = open("./breedingData-noheader.csv", 'wt', newline='')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
