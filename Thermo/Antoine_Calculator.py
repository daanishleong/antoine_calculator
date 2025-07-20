import pandas as pd
import math 
#loading of antoine coefficient table
coeffTable = pd.read_excel('/Users/daanishaqeefleong/Documents/ChemEng Projects/Data/Antoine_Coefficient.xlsx')
coeffTable['Name'] = coeffTable['Name'].str.strip().str.lower() #Faced a bug where typing certain chemicals made the code return None. Code to standardize the name column

#Use Antoine Equation to calculate out the vapor pressure at sspecific temperatures.
#What we need: User input on chemical species (A & B) as well as the temperature they want to investigate.
#Get the respective A, B and C from coeffTable 
def antoine_parameter(name):
    name = name.strip().lower()
    row = coeffTable[coeffTable['Name'] == name] 
    if not row.empty:
        return row[['Antoine_A', 'Antoine_B', 'Antoine_C']].values[0] 
    else:
        return None
#values = antoine_parameter(input(': ').title())
#print(values[0])

#calcualate out the vapor pressure
def vapor_pressure(speciesA, speciesB, T):
    valid_A = antoine_parameter(speciesA)
    valid_B = antoine_parameter(speciesB)
#Check if the species is valid as dataframe does not contain all chemical species
    if valid_A is None:
        return f"Species {speciesA} not found in DataFrame"
    if valid_B is None:
        return f"Species {speciesB} not found in DataFrame"

#If Species is valid extract out the respective A,B and C parameters
    specA_A = (antoine_parameter(speciesA)[0])
    specA_B = (antoine_parameter(speciesA)[1])
    specA_C = (antoine_parameter(speciesA)[2])

    specB_A = (antoine_parameter(speciesB)[0])
    specB_B = (antoine_parameter(speciesB)[1])
    specB_C = (antoine_parameter(speciesB)[2])

#Calculate out vapor pressure for species A and B respectively. Note: Pressure is in kPa
    vapor_pressure_A = math.exp(specA_A - (specA_B/(T + specA_C)))
    vapor_pressure_B = math.exp(specB_A - (specB_B/(T + specB_C)))

    return (f'Vapor pressure for A: {vapor_pressure_A} kPa. Vapor Pressure for B: {vapor_pressure_B} kPa')

def unique_vapor_pressure(A, T):
    param_A = antoine_parameter(A)

    if param_A is None:
        return f"Species {A} not found in DataFrame"
    
    a_1, a_2, a_3 = param_A
    u_vape = math.exp(a_1 - (a_2/(T + a_3)))
    return u_vape


#testing
if __name__ == "__main__":
    A = input('Species A: ')
    B = input('Species B: ')
    T = float(input('Temperature in Celcius: '))
    print(vapor_pressure(A, B, T))


'''
Key takeaways and learnings:
1. File takes a while to load in. I do wonder if its due to the fact that im trying to load in an entire .xlsx file?
   Maybe i can try to make it so that only the selected rows and cols are applied at the start?
2. OOP. Learnt about OOP and how to open datasheets using pandas. Learnt about paths and how proper storage of files
   on the device is necessary. For example, if the pathway is unclear, pandas cannot read the sheet etc.
'''
