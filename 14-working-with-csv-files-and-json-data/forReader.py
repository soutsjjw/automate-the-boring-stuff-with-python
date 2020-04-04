import csv

with open('example.csv') as exampleFile:
    exampleReader = csv.reader(exampleFile)
    for row in exampleReader:
        print('Row #' + str(exampleReader.line_num) + ' ' + str(row))