from classes.Participant import Participant
from classes.Team import Team
import openpyxl
from openpyxl.styles import NamedStyle, Font, Border, Side

'''book = openpyxl.open("first.xlsx", read_only=True)
sheet = book.active'''

#workbook = openpyxl.load_workbook("start.xlsx")
#print(sheet["i26"].value)

wb = openpyxl.Workbook()
wb.create_sheet(title = 'Первый лист', index = 0)
# получаем лист, с которым будем работать
sheet = wb['Первый лист']

# создаем именованный стиль
ns = NamedStyle(name='highlight')
ns.font = Font(bold=True, size=20)
border = Side(style='thick', color='000000')
ns.border = Border(left=border, top=border, right=border, bottom=border)

#sheet['A1'].style = 'highlight'



# записываем файл
wb.save('start.xlsx')

wb.add_named_style(ns)



