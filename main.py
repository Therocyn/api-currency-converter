import matplotlib
import requests, csv
from time import ctime

fieldnames = ["Day of the week", "Month", "Day", "Time", "Year", "Currency"]
create_header = False
file_read=[]


try:
    with open("currency.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
            
        for row in reader:
            file_read.append(row)
        
        if file_read[0] != fieldnames:
            create_header = True
            
            
except FileNotFoundError:
    create_header = True
    print("File not found, creating csv file:")
    pass


with open("currency.csv", "a", encoding="utf-8", newline="") as file:
    url =  "https://v6.exchangerate-api.com/v6/a0ce73021b78d0c390e89f2f/latest/USD"
    reader = requests.get(url)
    data =  reader.json()
    time = ctime().split(sep=" ")
    time.remove("")
    time.append(data["conversion_rates"]["BRL"])
        
    row ={}
    for i in range(0,len(fieldnames)):
        row[fieldnames[i]] = time[i]
    
    
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    if create_header:
        writer.writeheader()
    
    writer.writerow(row)

if not create_header: 
    print(f'Last Update: {file_read[-1][0]}, {file_read[-1][1]} {file_read[-1][2]}th, {file_read[-1][4]}. Time: {file_read[-1][3]}. \
USD to BRL Quotation: R${file_read[-1][-1]}')
    print(f'Updated quotation: R${list(row.values())[-1]}')
else:
    print(f'Updated quotation: R${list(row.values())[-1]}')