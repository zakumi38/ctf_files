import re
from itertools import *
from math import floor
from watchfiles import run_process
from subprocess import check_output

 
name_list = []
point_list = []
def HalfRoundUp(value):
    return floor(value + 0.5)

def check_index(point_list:list,current_val:int) -> int:
    for index,val in enumerate(point_list): 
        if val < current_val: continue
        else:
            # count = point_list.count(val)
            # if count > 1: 
            #     return index + (count - 1) 
            return index 
            
def banker_rounding(digit:float) -> int:
    if digit < 1.5:
        return 

with open("data.txt","r") as f:
    pivot = 0
    pivot_name = ""
    for i in range(204):
        line = f.readline()
        name = " ".join(re.findall("[a-z]+",line,flags=re.IGNORECASE))
        ability = re.findall("[0-9]+",line)
        # ability = [ 8,10,10,1,1,10]
        if not ability: continue
        ability_weight = lambda s,skill_weight:round(6 * (int(s) * skill_weight)) + 10
        # ability_point = sum([int(i) for i in ability])  # without any manipulation
        # banker_rounding = lambda x: round(x) if x < 1.5 else round(x + 1)
        weights = [0.2,0.3,0.1,0.05,0.05,0.3]
        multiplier = [0.18,0.20,0.21,0.08,0.17,0.16]
        health,agility,charisma,knowledge,energy,resourcefulness = [ability_weight(val,weights[index])*multiplier[index] for index,val in enumerate(ability)]
        overall_value = round(5 * (health + agility  + charisma  + knowledge + energy + resourcefulness))
        # command = "java "
        # overall_value = check_output("java ./Main.java " + " ".join(ability),shell=True).decode()
        overall_value = int(overall_value)
        if overall_value > pivot:
            pivot = overall_value
            pivot_name = name
            point_list.append(overall_value)
            name_list.append(name)
        else:
            index:int = check_index(point_list,overall_value)
            point_list.insert(index,overall_value)
            name_list.insert(index,name)
count = 0
for i in reversed(range(len(name_list))):
    count += 1
    if count == 15:break
    print(name_list[i] + " -" ,point_list[i],end=", ")

# <skill>_score = round(6 * (int(s) * <skill>_weight)) + 10
# overall_value = round(5 * ((health * 0.18) + (agility * 0.20) + (charisma * 0.21) + (knowledge * 0.08) + (energy * 0.17) + (resourcefulness * 0.16)))
# 	Note: The round() function here is Python 3's round(), which uses a concept called Banker's Rounding

# name_books = dict(zip(name_list,point_list))
# print(yaml.dump(name_books))
