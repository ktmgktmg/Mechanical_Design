# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 13:27:58 2024

@author: ssn24
"""


import csv
from tabulate import tabulate

# Table 14_1

symbol_list = []
headers_14_1 = ["Symbol", "Name"]
with open('Gear_design_symbols.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        symbol_list.append(row)
symbol_dict = dict(symbol_list)
#print(dict(symbol_list))
print("Table 14-1 Symbols and Their Names ", tabulate(symbol_list, headers_14_1, tablefmt = "grid"))
#print(symbol_dict["C_e"])


# Table 14_2

Lewis_Factor_Y = []
headers_14_2_Y = ["Number of Teeth", "Y"]
with open('LewisFormFactor_Y.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        Lewis_Factor_Y.append(row)
Y_dict = dict(Lewis_Factor_Y)
print("Table 14-2 Values of the Lewis Form Factor Y (These Values Are for a Normal Pressure Angle of 20 degree,",
      "Full-Depth Teeth, and a Diametral Pitch of Unity in the Plane of Rotation)", 
      tabulate(Lewis_Factor_Y, headers_14_2_Y, tablefmt = "grid"))
print(Y_dict)



import pandas as pd
# Adjust display settings to show all columns
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)        # Adjust the width to fit all colum
#Table 14_3
# Data
data = {
    "Material Designation": ["Steel", "Steel", "Steel", "Steel", "Steel", "Nitralloy 135M, Nitralloy N, and 2.5% chrome (no aluminum)"],
    "Heat Treatment": [
        "Through-hardened", 
        "Flame or induction hardened with type A pattern",
        "Flame or induction hardened with type B pattern",
        "Carburized and hardened",
        "Nitrided (through-hardened steels)",
        "Nitrided"
    ],
    "Minimum Surface Hardness": [
        "See Fig.14-2", " See Table 8", "See Table 8", "See Table 9", "83.5 HR15N", "87.5 HR15N"
    ],
    "Gear Bending Strength S_t (psi/MPa) - Grade 1": [
        "See Fig. 14-2", " 45000 (310)", "22000 (151)", "55000 (380)", "See Fig. 14-3", "See Fig. 14-4"
    ],
    "Gear Bending Strength S_t (psi/MPa) - Grade 2": [
        "See Fig. 14-2", " 55000 (380)", "22000 (151)", "65000 (448) or 70000 (482)", "See Fig. 14-3", "See Fig. 14-4"
    ],
    "Gear Bending Strength S_t (psi/MPa) - Grade 3": [
        "—", "—", "—", "75000 (517)", "—", "See Fig.14-4"
    ]
}

# Creating DataFrame
table14_3 = pd.DataFrame(data)

# Display the DataFrame
print("Table 14-3 Repeatedly Applied Gear Bending Strength St at 10^7 Cycles and 0.99 Reliability for Steel Gears",table14_3)

# Convert to string and print
print(table14_3.to_string())

#Table 14_4

#largest surface pressure
import math

def largest_surface_pressure(F, b, l):
    p_max = (2 * F) / (math.pi * b * l)
    return p_max

E = 100
d =20
m = 10
p_max = largest_surface_pressure(E,d,m)
print(p_max)