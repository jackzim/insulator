from logging import raiseExceptions
import re
from itertools import chain
from part_dictionaries import *

def strip_number(part_number):
    part_list = part_number.split("-")
    return part_list

def electrical_coding(parts_list):
    electrical_code = parts_list[1]
    amperage = int(electrical_code[:-2]) * 100
    voltage_library = {1 : "120/240V", 2 : "120/240 Delta", 3: "208/120V", 4: "480V", 5: "480/277V", 6: "600V"}
    voltage_code = electrical_code[2]
    enclosure_code = parts_list[1][3]
    error_check = voltage_code.isdigit()
    if error_check == False:
        return print("Invalid Part Number")
    else:
        voltage_code = int(voltage_code)
        if voltage_code not in range(-1, 7):
            return print("Invalid Part Number")
        else:
            voltage = voltage_library.get(voltage_code)
            return amperage, voltage, voltage_code, enclosure_code

def identify_adders(parts_list, voltage_code):
    if len(parts_list) == 4:
        adder_code = parts_list[3]
        adders = re.sub('[EGIJKLORSUVWXYZ1234567890]', '', adder_code)
        adders = list(adders)
        adders = [adder.replace("P", "P" + str(voltage_code)) for adder in adders]
    elif len(parts_list) == 3:
        adders = []
    else:
        print("Invalid part number")
        adders = []
    return adders


def adder_part_list(adders):
    adder_parts = [adders_library[adder] for adder in adders]
    adder_flat_list = list(chain(*(adder if isinstance(adder, tuple) else (adder,) for adder in adder_parts)))
    return adder_flat_list

def wallmount_breaker_pull(one_line, amperage, is_100_percent_rated):
    if is_100_percent_rated == False:
        breaker_kit = w_breaker_library[str(amperage)]
        quantity = amount_of_breakers[one_line]
        for i in range (0, len(breaker_kit)):
            breaker_kit[i][1] = quantity * breaker_kit[i][1]
    else:
        breaker_kit = w_breaker_library_100[str(amperage)]
        quantity = amount_of_breakers[one_line]
        for i in range (0, len(breaker_kit)):
            breaker_kit[i][1] = quantity * breaker_kit[i][1]
    return breaker_kit, quantity

def full_tmts(amperage, voltage_code, part_list):
    letter_code = part_list[0]
    if letter_code in ["TMTS"]:
        tmts_kit = tmts_library[str(amperage)]
        if voltage_code == 1:
            tmts_kit[0][1] = tmts_kit[0][1] * 2
        else:
            tmts_kit[0][1] = tmts_kit[0][1] * 3
    else:
        tmts_kit = []
    return tmts_kit

def padmount_breaker_pull(one_line, amperage, is_100_percent_rated):
    if is_100_percent_rated == False:
        breaker_kit = p_745_library[str(amperage)]
        quantity = amount_of_breakers[one_line]
        for i in range (0, len(breaker_kit)):
            breaker_kit[i][1] = quantity * breaker_kit[i][1]
    else:
        breaker_kit = p_745_library[str(amperage)]
        quantity = amount_of_breakers[one_line]
        for i in range (0, len(breaker_kit)):
            breaker_kit[i][1] = quantity * breaker_kit[i][1]
    return breaker_kit, quantity

def ERMS(voltage_code, one_line, enclosure_code):
    if enclosure_code == "P":
        if voltage_code == 3:
            erms_list = [["ADPSB24060P", 1], ["DINDNEB35MN", 2], ["LFCCMR020.TXP", 1], ["LFL60030C1CDINR", 1], ["PC3032224", 2], ["PC3044102", 4], ["SD9001K11J35LLL", 1], ["SD9001K7", 1], ["SD9001KA1", 1], ["TS84158-001", 1]]
            quantity = amount_of_breakers[one_line]
            for i in range (0, len(erms_list)):
                erms_list[i][1] = quantity * erms_list[i][1]
        elif voltage_code == 5:
            erms_list = [["ADPSB24060S3", 1], ["DINDNEB35MN", 2], ["LFCCMR020.TXP", 3], ["LFL60030C3CDINR", 1], ["PC3032224", 2], ["PC3044102", 4], ["SD9001K11J35LLL", 1], ["SD9001K7", 1], ["SD9001KA1", 1], ["TS84158-001", 1]]
            quantity = amount_of_breakers[one_line]
            for i in range (0, len(erms_list)):
                erms_list[i][1] = quantity * erms_list[i][1]
    else:
        if voltage_code == 3:
            erms_list = [["ADPSB24060S3", 1], ["DINDNEB35MN", 2], ["LFCCMR020.TXP", 1], ["LFL60030C1CDINR", 1], ["PC3032224", 6], ["PC3044102", 6], ["SD9001K11J35LLL", 1], ["SD9001K7", 1], ["SD9001KA1", 1], ["SI3VA9977-OUF10", 1]]
            quantity = amount_of_breakers[one_line]
            for i in range (0, len(erms_list)):
                erms_list[i][1] = quantity * erms_list[i][1]
        elif voltage_code == 5:
            erms_list = [["ADPSB24060S3", 1], ["DINDNEB35MN", 2], ["LFCCMR020.TXP", 3], ["LFL60030C3CDINR", 1], ["PC3032224", 6], ["PC3044102", 6], ["SD9001K11J35LLL", 1], ["SD9001K7", 1], ["SD9001KA1", 1], ["SI3VA9977-OUF10", 1]]
            quantity = amount_of_breakers[one_line]
            for i in range (0, len(erms_list)):
                erms_list[i][1] = quantity * erms_list[i][1]
    return erms_list

def rotary_adders(part_list):
    letter_code = part_list[0]
    if letter_code in ["TMTS", "TATS"]:
        rotary_adders = [["ABBOA1G10", 2], ["ABBOA3G01", 2], ["DINDNEB35MN", 2], ["PC3044102", 8]]
    else:
        rotary_adders = []
    return rotary_adders

def phase_rotation_monitor(voltage_code):
    if voltage_code == 1:
        prm_list = [["TS81047-001", 1], ["TS81048-001", 1]]
    else:
        prm_list = [["LFKLKR.250", 3], ["LFLPSC0003ZXID", 1], ["SI3UG45121AR20", 1], ["TS81339-001", 1], ["TS81667-001", 1]]
    return prm_list

def internal_wiring(amperage, one_line, voltage_code, enclosure_code):
    if enclosure_code == "P":
        compressions = p_compression_lugs[str(amperage)]
        breaker_amount = amount_of_breakers[one_line]
        if breaker_amount == 0:
            compressions[1] = compressions[1] * 1
        elif breaker_amount == 1:
            compressions[1] = compressions[1] * 3
        elif breaker_amount == 2:
            compressions[1] = compressions[1] * 5
        else:
            print("Raise Error")
    elif enclosure_code == "W":
        compressions = compression_lug_library[str(amperage)]
        amount = w_compression_lug_locations[one_line]
        if voltage_code == 1:
            compressions[1] = compressions[1] * 2 * amount
        else:
            compressions[1] = compressions[1] * 3 * amount
    elif enclosure_code == "L":
        compressions = compression_lug_library[str(amperage)]
        amount = w_compression_lug_locations[one_line]
        if voltage_code == 1:
            compressions[1] = compressions[1] * 2 * amount
        else:
            compressions[1] = compressions[1] * 3 * amount
    return compressions

def split_list(full_list):
    epicor_list = [i[0] for i in full_list]
    quantity_list = [i[1] for i in full_list]
    quantity_list = [float(i) for i in quantity_list]
    return epicor_list, quantity_list

def flatten_duplicates(full_list):
    placeholderDict = {}
    for sub in full_list:
        key = sub[0]
        values = sub[1:]
        if key in placeholderDict:
            placeholderDict[key] = [i+j for i,j in zip(values, placeholderDict[key])]
        else:
            placeholderDict[key] = values
    final_list = [[k] + v for k,v in placeholderDict.items()]
    return final_list