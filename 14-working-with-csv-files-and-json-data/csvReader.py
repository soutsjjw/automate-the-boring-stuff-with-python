import csv

with open('example.csv') as exampleFile:
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    
    print(exampleData[0][0])
    print(exampleData[0][1])
    print(exampleData[0][2])
    print(exampleData[1][1])
    print(exampleData[6][1])