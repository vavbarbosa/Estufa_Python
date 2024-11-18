import xlsxwriter

workbook = xlsxwriter.Workbook('Dados_Estufa_27_02_2022)')
worksheet = workbook.add_worksheet("Sheet1")

temperaturas = (['27/02/2022',100],['27/02/2022',100],
                ['27/02/2022',100],['27/02/2022',100],['27/02/2022',100])


row = 0
col = 1
for name, temperatura in (temperaturas):
    worksheet.write(row, col, name)
    worksheet.write(row, col + 1, temperatura)
    row += 1
    
workbook.close()