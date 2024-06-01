from classes.Participant import Participant
from classes.Team import Team
import openpyxl
from openpyxl.styles import NamedStyle, Font, Border, Side
from openpyxl.styles import Alignment

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
#начинаем формирование шапки стартового фацла

sheet.merge_cells('A1:H1')
sheet['A1'].value = 'СТАРТОВЫЙ ПРОТОКОЛ'
sheet['A1'].alignment = Alignment(horizontal='center')

sheet.merge_cells('A2:H2')
sheet['A2'].value = 'СОРЕВНОВАНИЙ ПО ЛЫЖНЫМ ГОНКАМ'
sheet['A2'].alignment = Alignment(horizontal='center')

sheet.merge_cells('A3:H3')
sheet['A3'].value = 'СПАРТАКИАДЫ А'
sheet['A3'].alignment = Alignment(horizontal='center')

sheet.merge_cells('A4:H4')
#получаем группу соревнований
type_competition = 1
if (type_competition == 1):
    sheet['A4'].value = 'cреди постоянного состава'
if (type_competition == 2):
    sheet['A4'].value = 'cреди переменного состава (мужчины)'
if (type_competition == 3):
    sheet['A4'].value = 'cреди переменного состава (женщины)'
sheet['A4'].alignment = Alignment(horizontal='center')



# записываем файл
wb.save('start.xlsx')

wb.add_named_style(ns)



