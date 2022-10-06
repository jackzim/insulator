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
        sg.popup("Please Enter a Valid Part Number and One Line Combination")
    return purpose_validity

def modifier_valid(one_line, erms, is_100_percent_rated):
    amount = amount_of_breakers[one_line]
    if is_100_percent_rated or erms == True:
        if amount == 0:
            modifier_validity = False
            sg.popup("ERMS or 100% Rated Selected with no breakers")
        else:
            modifier_validity = True
    else:
        modifier_validity = True
    print(f"Mod: {modifier_validity}")
    return modifier_validity