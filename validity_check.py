from frontend import one_line, erms, is_100_percent_rated
from part_dictionaries import *
import re
import PySimpleGUI as sg

def purpose_matching(parts_list, one_line):
    purpose = parts_list[0]
    entered_purpose = re.sub('[-1234567890]', '', one_line)
    if purpose == entered_purpose:
        purpose_validity = True
    else:
        purpose_validity = False
        sg.popup("Please Enter a Valid Part Number and One Line Combination", icon = "image/trystar-mark.ico")
    return purpose_validity

def modifier_valid(one_line, erms, is_100_percent_rated):
    amount = amount_of_breakers[one_line]
    if is_100_percent_rated or erms == True:
        if amount == 0:
            modifier_validity = False
            sg.popup("ERMS or 100% Rated Selected with no breakers", icon = "image/trystar-mark.ico")
        else:
            modifier_validity = True
    else:
        modifier_validity = True
    print(f"Mod: {modifier_validity}")
    return modifier_validity

def invalid_checkbox(is_4P, is_100_percent_rated, enclosure_code):
    if is_4P == True and is_100_percent_rated == True:
        checkbox_validity = False
        sg.popup("100% Rated and 4P do not Currently Work Together", icon = "image/trystar-mark.ico")
    elif is_4P == True and enclosure_code == "P":
        checkbox_validity = False
        sg.popup("4P in Padmounts Not Supported Yet", icon = "image/trystar-mark.ico")
    else:
        checkbox_validity = True
    return checkbox_validity

