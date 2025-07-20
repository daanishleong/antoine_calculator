# Vapour phase: IDG if Psys < 10 bar
# Liquid phase: IDS if 2 species are chemically similar. How to code in chemically similar????

import pandas as pd
from Thermo.Antoine_Calculator import unique_vapor_pressure

#Load in chemically_similar sheet from data
c_similar = pd.read_excel('/Users/daanishaqeefleong/Documents/ChemEng Projects/Data/Antoine_Coefficient.xlsx', sheet_name = 'C_Similar')

# x1 = species A, x2 = species B, P = bubble pressure
def x_composition_raoults(P, T, x1, x2):
    P2_vap = unique_vapor_pressure(x2, T)
    P1_vap = unique_vapor_pressure(x1, T)
    return (P - P2_vap)/(P1_vap - P2_vap)

def y_composition_raoults(P, T, x1, x2):
    x_comp = x_composition_raoults(P, T, x1, x2)
    p1_vape = unique_vapor_pressure(x1, T)
    return (x_comp * p1_vape)/P

if __name__ == '__main__':
    print(x_composition_raoults(100, 95, 'benzene', 'toulene'))
    print(y_composition_raoults(100, 95, 'benzene', 'toulene'))




# Limitation: While we can implement a rough template for detecting chemical similarity, we are unable to determine activity 
# coefficient due to DOF. We need to solve for chemical composition ahead of time which we cannot do as it is still an unknown
# commom workaround is to solve a system of linear equations which aims to solve both AC and Comp simulatneously. Another
# possible approach is to maybe try for an optimization approach using ML or numpy (similar to utilising What-If analysis)
# on excel. 
'''
def best_model(P, species_1, species_2, T):
    s1 = species_1.strip().lower()
    s2 = species_2.strip().lower()

    mask = (
        ((c_similar['Species_1'].str.strip().str.lower() == s1) &
         (c_similar['Species_2'].str.strip().str.lower() == s2)
         |
          (c_similar['Species_1'].str.strip().str.lower() == s2) &
         (c_similar['Species_2'].str.strip().str.lower() == s1))
    )

    if c_similar[mask].shape[0] > 0 and P < 1000:
        return composition_raoults(P, species_1, species_2, T)
    else:
        return composition_m_raoults(P, species_1, species_2, T)

def composition_m_raoults(P_sys, x1, x2, T):
    P1_vap = unique_vapor_pressure(x1, T)
    P2_vap = unique_vapor_pressure(x2, T)
    return 
'''