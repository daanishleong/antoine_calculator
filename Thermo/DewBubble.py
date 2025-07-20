from Thermo.Antoine_Calculator import vapor_pressure, unique_vapor_pressure
from Thermo.composition import x_composition_raoults, y_composition_raoults

#bubble pressure: we need original flow composition (), new system pressure and temperature

def bubble_pressure(T_sys, species_1, species_2, x1, x2):
    #calculate out new vapour pressure @ system conditions 
    p1_vap = unique_vapor_pressure(species_1, T_sys)
    p2_vap = unique_vapor_pressure(species_2, T_sys)
    return (x1 * p1_vap) + (x2 * p2_vap)

def dew_pressure(T_sys, species_1, species_2, y1, y2):
    p1_vap = unique_vapor_pressure(species_1, T_sys)
    p2_vap = unique_vapor_pressure(species_2, T_sys)
    return 1 / ((y1 / p1_vap) + (y2 / p2_vap))

if __name__ == '__main__':
    print(bubble_pressure(75,'benzene', 'toulene', 0.388, 0.612))
    print(dew_pressure(75,'benzene', 'toulene', 0.388, 0.612))

    