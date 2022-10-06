from tkinter.font import BOLD
from tkinter.ttk import Style
import PySimpleGUI as sg

sg.theme('LightGrey')	
one_lines = [
"GDS-1", "GDS-2", "GDS-3", "GDS-4", "GDS-6", "SBDS-1", "SBDS-2", 
"SBDS-3", "SBDS-4", "SBDS-5", "SBDS-6", "SBDS-7", "DBDS-1", "DBDS-4",
 "DBDS-5", "DBDS-6", "TMTS-1", "TMTS-2", "TMTS-3", "TMTS-4", "TMTS-5", "TMTS-6"
]
search_column = [
	[sg.Text('Please Enter Part Number and One Line')],
	[sg.Text('Part Number', size = (15, 1))],
    [sg.InputText(background_color = "LightGrey", text_color = "Black")],
    [sg.Text('One Line', size = (15, 1))],
	[sg.Combo(one_lines, background_color = "LightGrey", text_color = "Black", size = (15,1))],
    [sg.Checkbox('100% Rated')],
    [sg.Checkbox('ERMS')],
	[sg.Submit(), sg.Cancel()]
]

image_column = [
    [sg.Image("trystar.png")],
    [sg.Text('Trystar Insulator', font = ('Berlin Sans FB', 12))] 
]

layout = [
    [sg.Column(search_column),
     sg.VSeperator(),
     sg.Column(image_column),]
]

window = sg.Window('Insulator', layout)
event, values = window.read()
window.close()

part_number = values[0]
one_line = values[1]
is_100_percent_rated = values[2]
erms = values[3]