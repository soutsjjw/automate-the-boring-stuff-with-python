import csv

with open('output.csv', 'w', newline='') as outputFile:
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
    outputWriter.writerow(['Hello world!', 'eggs', 'bacon', 'ham'])
    outputWriter.writerow([1, 2, 3.141592, 4])