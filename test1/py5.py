import xlwt
# 创建workbook对象
workbook = xlwt.Workbook(encoding="utf-8")
# 创建工作表
worksheet = workbook.add_sheet("sheet1")
# 写入数据，行，列，内容
# worksheet.write(0,0,"hello")
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d"%(j+1,i+1,(i+1)*(j+1)))
# 保存数据
workbook.save("student.xls")