import csv

with open('example.csv', 'w', newline='') as csvFile:
    csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
    csvWriter.writerow(['apples', 'oranges', 'grapes'])
    csvWriter.writerow(['eggs', 'bacon', 'ham'])
    csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])