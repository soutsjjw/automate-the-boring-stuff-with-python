import openpyxl
from openpyxl.chart import Reference, Series, BarChart

wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1, 11):  # create some data in column A
    sheet['A' + str(i)] = i

refObj = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)

seriesObj = Series(refObj, title='First series')

chartObj = BarChart()
chartObj.append(seriesObj)

'''
chartObj.drawing.top = 50
chartObj.drawing.left = 100
chartObj.drawing.width = 300
chartObj.drawing.height = 200
'''

sheet.add_chart(chartObj, 'C2')
wb.save('sampleChart.xlsx')
