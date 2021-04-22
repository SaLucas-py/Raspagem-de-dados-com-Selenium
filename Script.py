import xlsxwriter

file = xlsxwriter.Workbook('projeto1.xlsx')
table = file.add_worksheet()
a = 'A1'
b = 0
c = 'Produtos'
z = 'A'
m = 1


table.write(z,m,)

file.close()