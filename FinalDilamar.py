#The systems requried for running the code (pandas and matlib), as well as the data file are ebing uploaded so that the algorithim has access to them. 
import pandas as pd
data=pd.read_csv("data.csv")
data = data.dropna()
list=[]

#function 1 is designed to prompt the user for which energy they want. There is a match-case to account for user exceptions when they are answering the input question.

def fun1():
    x = input("Please input the energy type that you want to search for here. This will give you the top state for your selected energy type in gigawatts per hour (gwh):, the options are roof top pv, csp, on shore wind, off shore wind, solid biopower, gaseous biopower, hydropower, urban utility ").lower()
    match x : 
        case "roof top pv":
            x = "rooftoppv_gwh"
        case "csp":
            x = "csp_gwh"
        case "on shore wind":
            x = "onshorewind_gwh"
        case "off shore wind":
            x = "offshorewind_gwh"
        case "solid biopower":
            x = "biopowersolid_gwh"
        case "gaseous biopower":
            x = "biopowergaseous_gwh"
        case "geothermal and hydrothermal":
            x = "geothermalhydrothermal_gwh"
        case "enhanced geothermal systems":
            x = "egsgeothermal_gwh"
        case "hydropower":
            x = "hydropower_gwh"
        case "urban utility": 
            x = "urbanUtilityScale"
#Using a conditional, based on the user's input for the energy question, the algorithim will find which energy is desired and will print the state with the best value for that particular category.
    if x=="onshorewind_gwh":
        for i in data.values:
            list.append(i[12])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[12] == a:
                c = i[0]
                print(f"In {c} the on shore wind energy type capacity is {a} gwh")
                continue              
    elif x=="offshorewind_gwh":
        for i in data.values:
            list.append(i[15])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[15] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="urbanUtilityScale":
        for i in data.values:
            list.append(i[1])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[1] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="rooftoppv_gwh":
        for i in data.values:
            list.append(i[7])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[7] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="csp_gwh":
        for i in data.values:
            list.append(i[9])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[9] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="biopowersolid_gwh":
        for i in data.values:
            list.append(i[18])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[18] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="biopowergaseous_gwh":
        for i in data.values:
            list.append(i[21])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[21] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="geothermalhydrothermal_gwh":
        for i in data.values:
            list.append(i[24])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[24] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="egsgeothermal_gwh":
        for i in data.values:
            list.append(i[26])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[26] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="hydropower_gwh":
        for i in data.values:
            list.append(i[28])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[28] == a:
                c = i[0]
                print(c, a)
                continue
    elif x=="geothermalhydrothermal_gwh":
        for i in data.values:
            list.append(i[24])
        list.sort()
        a = list[len(list) - 1]
        for i in data.values:
            if i[24] == a:
                c = i[0]
                print(c, a)
                continue
    elif x == "q":
        print("You have exited the program")
    else: 
        print("Try again, make sure to get the correct energy type name")


#Fucntion 2 will prompt the user to select a state and then select the energy they want to search for in that state. 
def fun2():
    user_pick_state = input("Which state in the USA do you want to search for an energy type in? ").title()
    search_states_energy = input(f"What energy source in gigawatts per hour (gwh) do you want to look at in {user_pick_state}? possible energy sources, roof top pv, csp, on show wind, off shore wind, solid biopower, gaseous biopower, urban utility: ").lower()
    match search_states_energy : 
        case "roof top pv":
            search_states_energy = "rooftoppv_gwh"
        case "csp":
            search_states_energy = "csp_gwh"
        case "on shore wind":
            search_states_energy = "onshorewind_gwh"
        case "off shore wind":
            search_states_energy = "offshorewind_gwh"
        case "solid biopower":
            search_states_energy = "biopowersolid_gwh"
        case "gaseous biopower":
            search_states_energy = "biopowergaseous_gwh"
        case "geothermal and hydrothermal":
            search_states_energy = "geothermalhydrothermal_gwh"
        case "enhanced geothermal systems":
            search_states_energy = "egsgeothermal_gwh"
        case "hydropower":
            search_states_energy = "hydropower_gwh"
        case "urban utility": 
            search_states_energy = "urbanUtilityScale"
    for i in data.values:
        if i[0]== user_pick_state:
            if search_states_energy == "onshorewind_gwh":
                print(f"In {user_pick_state} the on shore wind energy type capacity is {i[12]} gwh")
            elif search_states_energy == "offshorewind_gwh":
                print(f"In {user_pick_state} the off shore wind energy type capacity is {i[15]} gwh")
            elif search_states_energy == "urbanUtilityScale":
                print(f"In {user_pick_state} the urban utility energy type capacity is {i[1]} gwh")
            elif search_states_energy == "rooftoppv_gwh":
                print(f"In {user_pick_state} the roof top pv energy type capacity is {i[7]} gwh")
            elif search_states_energy == "csp_gwh":
                print(f"In {user_pick_state} the csp energy type capacity is {i[9]} gwh")
            elif search_states_energy == "biopowersolid_gwh":
                print(f"In {user_pick_state} the solid biopower energy type capacity is {i[18]} gwh")
            elif search_states_energy == "biopowergaseous_gwh":
                print(f"In {user_pick_state} the gaseous biopower energy type capacity is {i[21]} gwh")
            elif search_states_energy == "geothermalhydrothermal_gwh":
                print(f"In {user_pick_state} the geothermal and hydrothermal energy type capacity is {i[24]} gwh")
            elif search_states_energy == "egsgeothermal_gwh":
                print(i[26])
            elif search_states_energy == "hydropower_gwh":
                print(i[28])
            else:
                print("Try Again.")

search_states_energy = input("What function do you want to use? Select '1' to recieve information of the best state for each energy type in each category. Select '2' to personally gather infomration about specific energy types for a state of your choosing. ")

#This conditional will help to indentify whcih version of the algorithim the user wants to run. 
if search_states_energy == "1":
    fun1()

if search_states_energy == "2": 
    fun2()
